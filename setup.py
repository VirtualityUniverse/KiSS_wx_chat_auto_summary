import sys
from cx_Freeze import setup, Executable

# 依赖项
build_exe_options = {
    "packages": ["os", "requests", "google.generativeai", "tqdm", "tkinter", "datetime", "json", "sys", "webbrowser", "subprocess", "logging", "pathlib"],
    "excludes": [],
    "include_files": [
        "cfg.py",
        "prompt/",
        "chatlog/",
        "output/",
        "logs/"
    ]
}

# 可执行文件
base = None
if sys.platform == "win32":
    base = "Win32GUI"  # 使用Windows GUI

setup(
    name="微信群聊自动摘要工具",
    version="1.0",
    description="微信群聊天记录提取、分析和可视化工具",
    options={"build_exe": build_exe_options},
    executables=[Executable("demo.py", base=base, target_name="微信群聊自动摘要.exe", icon="icon.ico")]
)