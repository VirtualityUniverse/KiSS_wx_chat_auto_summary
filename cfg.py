"""
微信群聊天记录提取、分析和可视化工具配置文件

此文件包含程序运行所需的所有默认配置参数
"""

# 应用默认设置
CHAT_DEMO_CFG = {
    **{
        "api_key": "AIzaSyAycf8ZNdXcMBRTGILPS64UCtoqNzTbeBc",  # 填写【Google Gemini】的 API Key。  （此处为我自用key，仅供测试，有效期较短，请自行申请）
        "prompt_template_path": r"./prompt/微信聊天记录可视化prompt.txt",  # Prompt地址
    },
    **{
        **{  # 微信4.x配置
            "wechat_data_dir": r"D:/Users/Administrator/Documents/xwechat_files/wxid_km81v7w6fe9422_0d04",
            "chatlog_work_dir": r"C:/Users/Administrator/Documents/chatlog/wxid_km81v7w6fe9422_0d04",
            "wx_version": "4",
        },
        **{  # 3.x 微信
            # "wechat_data_dir": r"D:/Users/Administrator/Documents/WeChat Files/wxid_xxxx",  # 【chatlog需要】
            # "chatlog_work_dir": r"C:/Users/Administrator/Documents/chatlog/wxid_xxxx",  # 【chatlog需要】
            # "wx_version": "3",
        },
    },
    "talkers": [  # 联系人、群聊  的【名称】、【wxid】，一般填【名称】即可。
        "创新点子", "AIGC精英分队㉖🚎🚌", "AI开发者创造营⚽️🏀🏐", "Simonlin的兄弟姐妹",
    ],
    # ——————————————————————————————————————
    # ——————————————————————————————————————
    # ——————————————————————————————————————
    **{
        "chatlog_server_ip_port": "127.0.0.1:5036",  # 服务器IP地址，与下方【chatlog_server_url】保持一致
        "chatlog_server_url": "http://127.0.0.1:5036",  # 服务器API地址
        "output_dir": r"./output",  # 输出的html地址
        "auto_open_browser": True,  # 是否自动打开浏览器
        "chatlog_exe_path": "./chatlog/chatlog.exe",  # 开源项目chatlog的exe可执行程序。
        "manual_gui_auto_decryption": True,  # 是否需要手动启动GUI以获取最新数据
        "manual_gui_auto_decryption_wait_sec": 30,  # 等待N秒，秒数
    },
    **{  # 日志配置
        "log_dir": './logs',
        "logging_level": "INFO",
        "logging_format": '%(asctime)s - %(levelname)s - %(message)s',
        "logging_date_format": '%Y-%m-%d %H:%M:%S'
    },

}
