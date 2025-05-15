import os
import sys
import subprocess
import tkinter as tk
from tkinter import messagebox

def check_environment():
    """检查环境是否满足要求"""
    # 检查chatlog.exe是否存在
    if not os.path.exists("chatlog/chatlog.exe"):
        return False, "未找到chatlog.exe，请确保chatlog目录下有chatlog.exe文件"
    
    # 检查配置文件
    if not os.path.exists("cfg.py"):
        return False, "未找到cfg.py配置文件"
    
    # 检查prompt目录
    if not os.path.exists("prompt"):
        return False, "未找到prompt目录"
    
    return True, "环境检查通过"

def main():
    """主函数"""
    # 创建必要的目录
    os.makedirs("logs", exist_ok=True)
    os.makedirs("output", exist_ok=True)
    
    # 检查环境
    env_ok, message = check_environment()
    if not env_ok:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("环境检查失败", message)
        sys.exit(1)
    
    # 启动主程序
    try:
        import demo
        demo.main()
    except Exception as e:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("运行错误", f"程序运行出错：{str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()