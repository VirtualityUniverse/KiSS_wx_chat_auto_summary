#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
微信群聊日报生成定时任务脚本
每天早上8点自动运行demo.py生成群聊日报
"""

import schedule
import time
import subprocess
import sys
import os
import logging
import threading
from datetime import datetime

# 配置日志
log_dir = './logs'
os.makedirs(log_dir, exist_ok=True)
log_filename = f"{log_dir}/scheduler_{datetime.now().strftime('%Y%m%d')}.log"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler(log_filename, encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# 定时任务配置
SCHEDULED_TIME = "08:00"  # 每天定时执行的时间
INPUT_TIMEOUT = 30  # 用户输入超时时间（秒）

def run_daily_report():
    """执行每日报告生成任务"""
    try:
        logger.info("开始执行每日群聊日报生成任务...")
        
        # 获取脚本所在目录的绝对路径
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # 构建demo.py的完整路径
        demo_script = os.path.join(script_dir, 'demo.py')
        
        # 构建命令行参数
        cmd = [sys.executable, demo_script, '--days', '1', '--output-dir', './output', '--generate-png', '--generate-url', '--auto-mode']
        
        # 执行命令
        logger.info(f"执行命令: {' '.join(cmd)}")
        process = subprocess.Popen(
            cmd, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE,
            text=True,
            encoding='utf-8'  # 明确指定使用UTF-8编码
        )
        
        # 获取输出
        stdout, stderr = process.communicate()
        
        # 记录输出
        if stdout:
            logger.info(f"标准输出:\n{stdout}")
        if stderr:
            logger.error(f"标准错误:\n{stderr}")
            
        # 检查执行结果
        if process.returncode == 0:
            logger.info("群聊日报生成任务执行成功")
            
            # 创建汇总报告URL文件
            create_summary_report()
        else:
            logger.error(f"群聊日报生成任务执行失败，返回码: {process.returncode}")
            
    except Exception as e:
        logger.error(f"执行群聊日报生成任务时出错: {str(e)}")

def create_summary_report():
    """创建汇总报告URL文件"""
    try:
        # 获取当前日期
        current_date = datetime.now().strftime("%Y-%m-%d")
        
        # 创建输出目录
        output_dir = os.path.join('./output', current_date)
        os.makedirs(output_dir, exist_ok=True)
        
        # 创建汇总报告文件路径
        summary_file = os.path.join(output_dir, f"all_reports_urls_{current_date}.txt")
        
        # 准备写入的内容
        content = f"===== 群日报发布信息汇总 ({current_date}) =====\n\n"
        content += f"生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        
        # 查找所有HTML和PNG文件
        html_files = []
        for root, _, files in os.walk(output_dir):
            for file in files:
                if file.endswith('.html'):
                    html_files.append(os.path.join(root, file))
        
        # 添加每个群日报的信息
        for i, html_file in enumerate(html_files, 1):
            # 获取文件名（不含扩展名）作为群名称
            file_name = os.path.basename(html_file)
            talker_name = os.path.splitext(file_name)[0]
            
            # 检查对应的PNG文件是否存在
            png_file = os.path.splitext(html_file)[0] + '.png'
            has_png = os.path.exists(png_file)
            
            # 检查对应的URL文件是否存在
            url_file = os.path.splitext(html_file)[0] + '.url'
            url_content = None
            if os.path.exists(url_file):
                with open(url_file, 'r', encoding='utf-8') as f:
                    url_content = f.read().strip()
            
            # 添加到汇总内容
            content += f"--- 群日报 #{i} ---\n"
            content += f"群聊名称: {talker_name}\n"
            content += f"HTML文件: {os.path.abspath(html_file)}\n"
            
            if url_content:
                content += f"发布地址(URL): {url_content}\n"
            
            if has_png:
                content += f"PNG图片地址: {os.path.abspath(png_file)}\n"
            
            content += "\n"
        
        # 写入文件
        with open(summary_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        logger.info(f"已创建群日报汇总文件: {summary_file}")
        
    except Exception as e:
        logger.error(f"创建汇总报告时出错: {str(e)}")

def get_input_with_timeout(prompt, timeout):
    """带超时的用户输入函数"""
    result = [None]
    
    def get_input():
        result[0] = input(prompt)
    
    # 创建输入线程
    input_thread = threading.Thread(target=get_input)
    input_thread.daemon = True
    input_thread.start()
    
    # 等待输入，最多等待timeout秒
    input_thread.join(timeout)
    
    # 如果线程还活着，说明超时了
    if input_thread.is_alive():
        print(f"\n输入超时（{timeout}秒），默认选择取消")
        return 'n'  # 默认返回'n'
    
    return result[0]

def main():
    """主函数，设置定时任务"""
    logger.info("启动微信群聊日报生成定时任务")
    
    # 设置每天早上指定时间执行任务
    schedule.every().day.at(SCHEDULED_TIME).do(run_daily_report)
    
    logger.info(f"定时任务已设置，将在每天早上{SCHEDULED_TIME}执行")
    logger.info("程序将持续运行，请勿关闭窗口")
    
    # 如果当前时间已过设定时间，可以选择立即执行一次
    current_hour = datetime.now().hour
    scheduled_hour = int(SCHEDULED_TIME.split(':')[0])
    
    if current_hour >= scheduled_hour:
        logger.info(f"当前时间已过{SCHEDULED_TIME}，是否要立即执行一次任务？(y/n)，{INPUT_TIMEOUT}秒内未输入则默认执行")
        choice = get_input_with_timeout(f"当前时间已过{SCHEDULED_TIME}，是否要立即执行一次任务？(y/n)，{INPUT_TIMEOUT}秒内未输入则默认执行: ", INPUT_TIMEOUT)
        
        if choice and choice.lower() == 'y':
            logger.info("用户选择立即执行任务")
            run_daily_report()
        else:
            if choice and choice.lower() == 'n':
                logger.info("用户选择不执行任务")
            else:
                logger.info("用户未做选择或选择取消，不执行任务")
    
    # 无限循环，持续检查是否有定时任务需要执行
    while True:
        schedule.run_pending()
        time.sleep(60)  # 每分钟检查一次

if __name__ == "__main__":
    main()