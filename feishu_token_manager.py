'''
飞书API令牌管理工具

功能描述:
自动管理飞书API的授权令牌(token)，包括获取、刷新和缓存令牌，
避免因令牌过期导致API调用失败。

使用方法:
1. 初始化TokenManager实例
2. 使用get_token()方法获取有效的授权令牌
3. 在API调用中使用该令牌

依赖安装:
pip install requests
'''

import requests
import json
import time
import logging
import os
from datetime import datetime, timedelta
from threading import Lock

# 配置日志
logger = logging.getLogger(__name__)

class FeishuTokenManager:
    """
    飞书API令牌管理器
    
    负责获取、刷新和缓存飞书API的授权令牌，确保API调用时使用有效的令牌。
    支持tenant_access_token和user_access_token两种类型的令牌。
    """
    
    def __init__(self, app_id=None, app_secret=None, config_module=None):
        """
        初始化令牌管理器
        
        参数:
            app_id (str): 飞书应用ID
            app_secret (str): 飞书应用密钥
            config_module (module): 包含飞书配置的模块，如果提供，将从中读取app_id和app_secret
        """
        self.app_id = app_id
        self.app_secret = app_secret
        self.config_module = config_module
        
        # 从配置模块加载配置
        if config_module is None:
            try:
                from cfg import CHAT_DEMO_CFG
                self.config = CHAT_DEMO_CFG
            except ImportError:
                self.config = {}
                logger.warning("无法导入配置模块，将使用默认值或传入的参数")
        else:
            self.config = config_module
            
        # 如果未提供app_id和app_secret，尝试从配置中读取
        if self.app_id is None:
            self.app_id = self.config.get('feishu_app_id', '')
        if self.app_secret is None:
            self.app_secret = self.config.get('feishu_app_secret', '')
            
        # 令牌缓存
        self._tenant_token = None  # 租户授权令牌
        self._tenant_token_expire_time = 0  # 租户令牌过期时间戳
        self._user_token = None  # 用户授权令牌
        self._user_token_expire_time = 0  # 用户令牌过期时间戳
        self._refresh_token = None  # 用于刷新用户令牌的刷新令牌
        
        # 线程锁，用于防止并发获取令牌
        self._lock = Lock()
        
        # 令牌文件路径
        self._token_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'feishu_token_cache.json')
        
        # 尝试从文件加载缓存的令牌
        self._load_tokens_from_file()
    
    def get_tenant_access_token(self, force_refresh=False):
        """
        获取有效的租户授权令牌(tenant_access_token)
        
        如果缓存中有未过期的令牌，则直接返回；否则获取新令牌
        
        参数:
            force_refresh (bool): 是否强制刷新令牌，即使缓存中的令牌未过期
            
        返回:
            str: 有效的租户授权令牌
        """
        with self._lock:
            current_time = time.time()
            
            # 检查是否需要刷新令牌
            if (not force_refresh and 
                self._tenant_token is not None and 
                current_time < self._tenant_token_expire_time - 300):  # 提前5分钟刷新
                return self._tenant_token
            
            # 需要获取新令牌
            try:
                url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
                headers = {"Content-Type": "application/json"}
                data = {
                    "app_id": self.app_id,
                    "app_secret": self.app_secret
                }
                
                response = requests.post(url, headers=headers, data=json.dumps(data))
                result = response.json()
                
                if response.status_code == 200 and result.get("code") == 0:
                    self._tenant_token = result.get("tenant_access_token")
                    # 计算过期时间（秒级时间戳）
                    expire_in = result.get("expire", 7200)  # 默认2小时
                    self._tenant_token_expire_time = current_time + expire_in
                    
                    # 保存令牌到文件
                    self._save_tokens_to_file()
                    
                    logger.info("成功获取新的tenant_access_token，有效期: %s秒", expire_in)
                    return self._tenant_token
                else:
                    logger.error("获取tenant_access_token失败: %s", result)
                    return None
            except Exception as e:
                logger.error("获取tenant_access_token时出错: %s", str(e))
                return None
    
    def get_user_access_token(self, code=None, refresh_token=None):
        """
        获取用户授权令牌(user_access_token)
        
        如果提供了code，则使用code获取新令牌；
        如果提供了refresh_token，则使用refresh_token刷新令牌；
        如果都未提供，则检查缓存中是否有有效令牌，有则返回，否则尝试使用缓存的refresh_token刷新。
        
        参数:
            code (str): 授权码，用于获取新的user_access_token
            refresh_token (str): 刷新令牌，用于刷新user_access_token
            
        返回:
            str: 有效的用户授权令牌
        """
        with self._lock:
            current_time = time.time()
            
            # 如果缓存中有未过期的令牌且未指定强制刷新，则直接返回
            if (code is None and refresh_token is None and 
                self._user_token is not None and 
                current_time < self._user_token_expire_time - 300):  # 提前5分钟刷新
                return self._user_token
            
            # 如果提供了code，则使用code获取新令牌
            if code is not None:
                return self._get_user_token_by_code(code)
            
            # 如果提供了refresh_token，则使用refresh_token刷新令牌
            if refresh_token is not None:
                self._refresh_token = refresh_token
            
            # 尝试使用缓存的refresh_token刷新令牌
            if self._refresh_token is not None:
                return self._refresh_user_token()
            
            # 无法获取有效令牌
            logger.error("无法获取user_access_token，需要提供code或refresh_token")
            return None
    
    def _get_user_token_by_code(self, code):
        """
        使用授权码获取用户授权令牌
        
        参数:
            code (str): 授权码
            
        返回:
            str: 用户授权令牌
        """
        try:
            url = "https://open.feishu.cn/open-apis/authen/v1/access_token"
            headers = {"Content-Type": "application/json"}
            data = {
                "grant_type": "authorization_code",
                "code": code,
                "app_id": self.app_id,
                "app_secret": self.app_secret
            }
            
            response = requests.post(url, headers=headers, data=json.dumps(data))
            result = response.json()
            
            if response.status_code == 200 and result.get("code") == 0:
                data = result.get("data", {})
                self._user_token = data.get("access_token")
                self._refresh_token = data.get("refresh_token")
                
                # 计算过期时间（秒级时间戳）
                expire_in = data.get("expires_in", 6900)  # 默认约1.9小时
                self._user_token_expire_time = time.time() + expire_in
                
                # 保存令牌到文件
                self._save_tokens_to_file()
                
                logger.info("成功获取新的user_access_token，有效期: %s秒", expire_in)
                return self._user_token
            else:
                logger.error("使用code获取user_access_token失败: %s", result)
                return None
        except Exception as e:
            logger.error("使用code获取user_access_token时出错: %s", str(e))
            return None
    
    def _refresh_user_token(self):
        """
        使用刷新令牌刷新用户授权令牌
        
        返回:
            str: 刷新后的用户授权令牌
        """
        try:
            url = "https://open.feishu.cn/open-apis/authen/v1/refresh_access_token"
            headers = {"Content-Type": "application/json"}
            data = {
                "grant_type": "refresh_token",
                "refresh_token": self._refresh_token,
                "app_id": self.app_id,
                "app_secret": self.app_secret
            }
            
            response = requests.post(url, headers=headers, data=json.dumps(data))
            result = response.json()
            
            if response.status_code == 200 and result.get("code") == 0:
                data = result.get("data", {})
                self._user_token = data.get("access_token")
                self._refresh_token = data.get("refresh_token")  # 更新刷新令牌
                
                # 计算过期时间（秒级时间戳）
                expire_in = data.get("expires_in", 6900)  # 默认约1.9小时
                self._user_token_expire_time = time.time() + expire_in
                
                # 保存令牌到文件
                self._save_tokens_to_file()
                
                logger.info("成功刷新user_access_token，有效期: %s秒", expire_in)
                return self._user_token
            else:
                logger.error("刷新user_access_token失败: %s", result)
                # 刷新失败，清除刷新令牌
                self._refresh_token = None
                self._save_tokens_to_file()
                return None
        except Exception as e:
            logger.error("刷新user_access_token时出错: %s", str(e))
            return None
    
    def _save_tokens_to_file(self):
        """
        将令牌信息保存到文件，用于持久化存储
        """
        try:
            token_data = {
                "tenant_token": self._tenant_token,
                "tenant_token_expire_time": self._tenant_token_expire_time,
                "user_token": self._user_token,
                "user_token_expire_time": self._user_token_expire_time,
                "refresh_token": self._refresh_token
            }
            
            with open(self._token_file, 'w') as f:
                json.dump(token_data, f)
                
            logger.debug("令牌信息已保存到文件")
        except Exception as e:
            logger.error("保存令牌信息到文件时出错: %s", str(e))
    
    def _load_tokens_from_file(self):
        """
        从文件加载令牌信息，用于恢复缓存的令牌
        """
        try:
            if os.path.exists(self._token_file):
                with open(self._token_file, 'r') as f:
                    token_data = json.load(f)
                    
                self._tenant_token = token_data.get("tenant_token")
                self._tenant_token_expire_time = token_data.get("tenant_token_expire_time", 0)
                self._user_token = token_data.get("user_token")
                self._user_token_expire_time = token_data.get("user_token_expire_time", 0)
                self._refresh_token = token_data.get("refresh_token")
                
                logger.debug("从文件加载令牌信息成功")
        except Exception as e:
            logger.error("从文件加载令牌信息时出错: %s", str(e))
    
    def clear_tokens(self):
        """
        清除所有缓存的令牌信息
        """
        with self._lock:
            self._tenant_token = None
            self._tenant_token_expire_time = 0
            self._user_token = None
            self._user_token_expire_time = 0
            self._refresh_token = None
            
            # 删除令牌文件
            if os.path.exists(self._token_file):
                try:
                    os.remove(self._token_file)
                    logger.info("令牌文件已删除")
                except Exception as e:
                    logger.error("删除令牌文件时出错: %s", str(e))

# 使用示例
def get_tenant_token_example():
    """
    获取租户授权令牌的示例
    """
    token_manager = FeishuTokenManager()
    token = token_manager.get_tenant_access_token()
    if token:
        print(f"获取到的tenant_access_token: {token}")
    else:
        print("获取tenant_access_token失败")

def get_user_token_example(code):
    """
    获取用户授权令牌的示例
    
    参数:
        code (str): 授权码
    """
    token_manager = FeishuTokenManager()
    token = token_manager.get_user_access_token(code=code)
    if token:
        print(f"获取到的user_access_token: {token}")
    else:
        print("获取user_access_token失败")

# 测试代码
if __name__ == "__main__":
    # 配置日志
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # 测试获取租户授权令牌
    get_tenant_token_example()