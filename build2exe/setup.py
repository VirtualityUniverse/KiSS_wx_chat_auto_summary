import os.path
import sys
from cx_Freeze import setup, Executable

# Add these lines
SETUP_PY_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SETUP_PY_DIR, '..'))
sys.path.insert(0, PROJECT_ROOT)

print("""

注意事项：
1、可通过  【  python build2exe/setup.py build  】  进行打包。
2、如果报错  【缺少socks包】  ，请参考以下注释，进行【pip install PySocks】安装。

目前存在的问题：
1、似乎，启动到 chatlog.exe 那一步，会黑屏、退出 （？）

""")

# 依赖项
build_exe_options = {
    "packages": [
        "os", "requests", "google.generativeai", "tqdm", "tkinter", "datetime", "json", "sys", "webbrowser", "subprocess", "logging", "pathlib",
        "socks",  # 需要通过【pip install PySocks】进行安装
    ],
    # "includes": ["cfg"],  # 此句为调试过程中产物，目前看来非必须。
    "excludes": [],
    "include_files": list(map(lambda p: os.path.join(PROJECT_ROOT, p), [  # Use PROJECT_ROOT
        "cfg.py",
        "prompt/",
        "chatlog/",
        "output/",
        "logs/"
    ]))
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
    executables=[Executable(
        os.path.join(PROJECT_ROOT, "demo.py"),  # Use PROJECT_ROOT
        base=base,
        icon=os.path.join(PROJECT_ROOT, "icon.ico"),  # Use PROJECT_ROOT for icon
        target_name="微信群聊自动摘要.exe",
    )]
)
