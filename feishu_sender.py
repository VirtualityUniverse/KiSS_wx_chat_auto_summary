'''
飞书多维表格API集成工具

功能描述:
自动将生成的群日报URL同步到飞书多维表格，实现数据归档和管理。
支持自动获取和刷新飞书授权令牌，避免因令牌过期导致API调用失败。

使用方法:
1. 确保已配置正确的飞书API访问凭证（app_token和table_id）
2. 调用send_url_to_feishu函数发送URL到飞书多维表格

依赖安装:
pip install requests
'''

import requests
import json
import uuid
from datetime import datetime
import logging

# 导入令牌管理器
from feishu_token_manager import FeishuTokenManager

# 配置日志
logger = logging.getLogger(__name__)

# 创建令牌管理器实例
token_manager = FeishuTokenManager()

def send_url_to_feishu(group_name, url, app_token=None, table_id=None, auth_token=None, retry_count=0):
    """
    将群日报URL发送到飞书多维表格
    
    参数:
        group_name (str): 微信群名称
        url (str): 群日报URL
        app_token (str): 飞书多维表格应用Token，默认从配置文件读取
        table_id (str): 飞书多维表格ID，默认从配置文件读取
        auth_token (str): 飞书API授权Token，默认使用令牌管理器获取
        retry_count (int): 当前重试次数，用于内部递归调用
    
    返回:
        bool: 发送成功返回True，否则返回False
    """
    # 最大重试次数
    MAX_RETRY = 2
    
    # 尝试导入配置
    try:
        from cfg import CHAT_DEMO_CFG
        # 如果未提供参数，则从配置文件读取
        if app_token is None:
            app_token = CHAT_DEMO_CFG.get('feishu_app_token', 'T87pbLkEman7EQsNRIoczyHsnHM')
        if table_id is None:
            table_id = CHAT_DEMO_CFG.get('feishu_table_id', 'tblEjyEQyBSLfpWq')
    except ImportError:
        # 如果无法导入配置，使用默认值
        if app_token is None:
            app_token = 'T87pbLkEman7EQsNRIoczyHsnHM'
        if table_id is None:
            table_id = 'tblEjyEQyBSLfpWq'
    
    # 如果未提供auth_token，使用令牌管理器获取
    if auth_token is None:
        # 如果是首次调用，使用缓存的令牌；如果是重试调用，强制刷新令牌
        force_refresh = retry_count > 0
        auth_token = token_manager.get_tenant_access_token(force_refresh=force_refresh)
        if not auth_token:
            logger.error("获取飞书授权令牌失败，无法同步到飞书")
            return False
    
    try:
        logger.info(f"准备将群聊 '{group_name}' 的URL同步到飞书: {url}")
        
        # 获取当前时间
        now = datetime.now()
        
        # 格式化当前时间
        formatted_now = now.strftime("%Y/%m/%d")
        
        # 生成随机UUID作为客户端令牌
        client_token = str(uuid.uuid4())
        
        # 构建API请求URL
        api_url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/records?client_token={client_token}&ignore_consistency_check=true&user_id_type=open_id"
        
        # 设置请求头
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {auth_token}'
        }
        
        # 构建请求数据
        payload = json.dumps({
            "fields": {
                "提交时间": formatted_now,
                "群消息日报URL链接": url,
                "群聊名称": group_name
            }
        })
        
        # 发送POST请求
        response = requests.request("POST", api_url, headers=headers, data=payload)
        response_json = response.json() if response.text else {}
        
        # 检查响应状态
        if response.status_code == 200 and response_json.get("code", -1) == 0:
            logger.info(f"成功将群聊 '{group_name}' 的URL同步到飞书")
            return True
        else:
            # 检查是否是令牌过期错误
            error_code = response_json.get("code", -1)
            if error_code in [99991663, 99991664] and retry_count < MAX_RETRY:  # 令牌过期或无效
                logger.warning(f"飞书授权令牌已过期，尝试刷新令牌并重试 (重试 {retry_count+1}/{MAX_RETRY})")
                # 递归调用自身，强制刷新令牌
                return send_url_to_feishu(group_name, url, app_token, table_id, None, retry_count + 1)
            
            logger.error(f"同步到飞书失败: {response.status_code}, {response.text}")
            return False
            
    except Exception as e:
        logger.error(f"将URL同步到飞书时出错: {str(e)}")
        return False

def send_urls_to_feishu_batch(reports_info):
    """
    批量将多个群日报URL发送到飞书多维表格
    
    参数:
        reports_info (list): 包含群日报信息的列表，每个元素是一个字典，包含群名称和URL
    
    返回:
        dict: 包含成功和失败数量的字典
    """
    try:
        success_count = 0
        failed_count = 0
        
        # 预先获取一次令牌，避免每次调用都获取
        auth_token = token_manager.get_tenant_access_token()
        if not auth_token:
            logger.error("获取飞书授权令牌失败，无法批量同步到飞书")
            return {'total': 0, 'success': 0, 'failed': 0}
        
        # 过滤有效的报告信息（包含URL和群聊名称）
        valid_reports = [r for r in reports_info if r.get('html_url') and r.get('talker')]
        
        for report in valid_reports:
            talker = report['talker']
            url = report['html_url']
            
            if send_url_to_feishu(talker, url, auth_token=auth_token):
                success_count += 1
            else:
                # 如果失败，尝试不传递auth_token，让函数内部重新获取
                if send_url_to_feishu(talker, url):
                    success_count += 1
                else:
                    failed_count += 1
                
        result = {
            'total': len(valid_reports),
            'success': success_count,
            'failed': failed_count
        }
        
        logger.info(f"飞书同步结果: 总计 {result['total']}, 成功 {result['success']}, 失败 {result['failed']}")
        return result
        
    except Exception as e:
        logger.error(f"批量同步到飞书时出错: {str(e)}")
        return {'total': 0, 'success': 0, 'failed': 0}

# 测试代码
if __name__ == "__main__":
    # 配置日志
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # 测试发送单个URL
    test_result = send_url_to_feishu("测试群", "https://example.com/report")
    print(f"测试结果: {'成功' if test_result else '失败'}")
    
    # 测试批量发送URL
    test_reports = [
        {
            'talker': '测试群1',
            'html_url': 'https://example.com/report1'
        },
        {
            'talker': '测试群2',
            'html_url': 'https://example.com/report2'
        }
    ]
    batch_result = send_urls_to_feishu_batch(test_reports)
    print(f"批量测试结果: 总计 {batch_result['total']}, 成功 {batch_result['success']}, 失败 {batch_result['failed']}")