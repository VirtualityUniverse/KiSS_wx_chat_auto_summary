'''
微信群日报URL自动发送工具

功能描述:
自动将生成的群日报URL发送到对应的微信群聊，减少手动操作。

使用方法:
1. 确保微信已登录并处于可用状态
2. 调用send_url_to_wechat_group函数发送URL到指定群聊

依赖安装:
pip install pyautogui pyperclip
'''

import time
import os
import logging
import pyautogui
import pyperclip

# 配置日志
logger = logging.getLogger(__name__)


def send_url_to_wechat_group(group_name, url, message_prefix="今日群日报已生成："):
    """
    将URL发送到指定的微信群聊
    
    参数:
        group_name (str): 微信群名称
        url (str): 要发送的URL
        message_prefix (str): URL前的消息前缀，默认为"今日群日报已生成："
    
    返回:
        bool: 发送成功返回True，否则返回False
    """
    try:
        logger.info(f"准备向群聊 '{group_name}' 发送URL: {url}")
        
        # 激活微信窗口
        activate_wechat_window()
        if not activate_wechat_window():
            logger.error("无法激活微信窗口")
            return False
        
        # 搜索并选择群聊
        if not search_and_select_chat(group_name):
            logger.error(f"无法找到群聊: {group_name}")
            return False
        
        # 组合完整消息
        full_message = f"{message_prefix}\n{url}"
        
        # 复制消息到剪贴板
        pyperclip.copy(full_message)
        
        # 粘贴消息
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)
        
        # 发送消息
        pyautogui.press('enter')
        
        logger.info(f"成功向群聊 '{group_name}' 发送URL")
        return True
        
    except Exception as e:
        logger.error(f"向群聊 '{group_name}' 发送URL时出错: {str(e)}")
        return False

def activate_wechat_window():
    """
    激活微信窗口
    
    返回:
        bool: 成功返回True，否则返回False
    """
    try:
        # 尝试查找微信窗口
        wechat_window = pyautogui.getWindowsWithTitle('微信')
        
        if not wechat_window:
            logger.warning("未找到微信窗口，请确保微信已打开")
            return False
        
        # 激活找到的第一个微信窗口
        wechat_window[0].activate()
        time.sleep(1)  # 等待窗口激活
        
        return True
    except Exception as e:
        # 检查错误消息，如果是Windows返回的成功状态码，则忽略此错误
        error_msg = str(e)
        if "Error code from Windows: 0 - 操作成功完成" in error_msg:
            logger.info("微信窗口激活成功，忽略Windows返回的成功状态码")
            return True
        else:
            logger.error(f"激活微信窗口时出错: {error_msg}")
            return False

def search_and_select_chat(chat_name):
    """
    搜索并选择指定的聊天会话
    
    参数:
        chat_name (str): 聊天会话名称
    
    返回:
        bool: 成功返回True，否则返回False
    """
    try:
        # 点击搜索框
        pyautogui.hotkey('ctrl', 'f')
        time.sleep(0.5)
        
        # 清空搜索框
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(0.2)
        pyautogui.press('delete')
        time.sleep(0.2)
        
        # 输入群聊名称
        pyperclip.copy(chat_name)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1.5)  # 等待搜索结果
        
        # 点击第一个搜索结果
        pyautogui.press('enter')
        time.sleep(1)  # 等待聊天窗口加载
        
        return True
    except Exception as e:
        logger.error(f"搜索并选择聊天会话时出错: {str(e)}")
        return False

def send_urls_from_file(urls_file, delay_between_groups=5):
    """
    从统一的URL文件中读取并发送URL到对应的微信群
    
    参数:
        urls_file (str): URL文件的路径
        delay_between_groups (int): 每个群发送后的延迟时间(秒)
    
    返回:
        bool: 全部发送成功返回True，否则返回False
    """
    try:
        if not os.path.exists(urls_file):
            logger.error(f"URL文件不存在: {urls_file}")
            return False
            
        with open(urls_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 解析文件内容
        reports = []
        current_report = {}
        
        for line in content.split('\n'):
            line = line.strip()
            
            if line.startswith('--- 群日报 #'):
                if current_report and 'talker' in current_report and 'html_url' in current_report:
                    reports.append(current_report)
                current_report = {}
            elif line.startswith('群聊名称:'):
                current_report['talker'] = line.replace('群聊名称:', '').strip()
            elif line.startswith('发布地址(URL):'):
                current_report['html_url'] = line.replace('发布地址(URL):', '').strip()
                
        # 添加最后一个报告
        if current_report and 'talker' in current_report and 'html_url' in current_report:
            reports.append(current_report)
            
        # 发送URL到对应群聊
        success_count = 0
        for report in reports:
            if send_url_to_wechat_group(report['talker'], report['html_url']):
                success_count += 1
                time.sleep(delay_between_groups)  # 每个群发送后等待一段时间
                
        logger.info(f"成功发送 {success_count}/{len(reports)} 个URL到微信群")
        return success_count == len(reports)
        
    except Exception as e:
        logger.error(f"从文件发送URL时出错: {str(e)}")
        return False

# 测试代码
if __name__ == "__main__":
    # 配置日志
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # 测试发送单个URL
    # send_url_to_wechat_group("测试群", "https://example.com/report")
    
    # 测试从文件发送URL
    # 获取当前日期作为文件名的一部分
    from datetime import datetime
    current_date = datetime.now().strftime("%Y-%m-%d")
    urls_file = f"./output/all_reports_urls_{current_date}.txt"
    
    if os.path.exists(urls_file):
        print(f"找到URL文件: {urls_file}，开始发送...")
        send_urls_from_file(urls_file)
    else:
        print(f"URL文件不存在: {urls_file}")
        # 列出output目录下的所有文件
        output_dir = "./output"
        if os.path.exists(output_dir):
            files = os.listdir(output_dir)
            url_files = [f for f in files if f.startswith("all_reports_urls_")]
            if url_files:
                print("找到以下URL文件:")
                for file in url_files:
                    print(f"  - {file}")
                latest_file = os.path.join(output_dir, sorted(url_files)[-1])
                print(f"\n使用最新的URL文件: {latest_file}")
                send_urls_from_file(latest_file)
            else:
                print(f"在 {output_dir} 目录下未找到任何URL文件")