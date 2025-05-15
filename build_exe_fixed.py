import os
import sys
import shutil
import PyInstaller.__main__

# 确保输出目录存在
if not os.path.exists("dist"):
    os.makedirs("dist")

# 确保必要的目录存在
for dir_name in ["logs", "output", "temp", "chatlog"]:
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

# 检查chatlog.exe是否存在
chatlog_exe = os.path.join("chatlog", "chatlog.exe")
if not os.path.exists(chatlog_exe):
    print(f"错误: 找不到 {chatlog_exe}，请确保该文件存在")
    sys.exit(1)

# 使用PyInstaller打包
PyInstaller.__main__.run([
    'demo.py',
    '--name=微信群聊自动摘要',
    '--onefile',
    '--console',  # 使用控制台模式便于查看错误
    '--add-data=cfg.py;.',
    '--add-data=chatlog;chatlog',
    '--add-data=prompt;prompt',
    '--add-data=output;output',
    '--add-data=logs;logs',
    '--add-data=temp;temp',
    '--hidden-import=google.generativeai',
    '--hidden-import=tqdm',
    '--hidden-import=requests',
    '--hidden-import=tkinter',
    '--exclude=PyQt5',
    '--exclude=PySide2',
])

# 复制必要的文件到dist目录
print("复制额外文件到dist目录...")
shutil.copy("cfg.py", os.path.join("dist", "cfg.py"))

# 创建启动批处理文件
with open(os.path.join("dist", "启动.bat"), "w", encoding="utf-8") as f:
    f.write('@echo off\n')
    f.write('echo 正在启动微信群聊自动摘要工具...\n')
    f.write('cd /d "%~dp0"\n')
    f.write('微信群聊自动摘要.exe\n')
    f.write('if %errorlevel% neq 0 (\n')
    f.write('    echo 程序运行出错，请按任意键退出\n')
    f.write('    pause > nul\n')
    f.write(')\n')

print("打包完成！可执行文件位于 dist 目录中。")