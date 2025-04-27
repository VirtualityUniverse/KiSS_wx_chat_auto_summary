"""
微信群聊天记录提取、分析和可视化工具

功能描述:
利用Gemini API自动获取、分析微信群聊记录并生成美观的HTML日报，帮助群成员快速了解群内重要信息与讨论内容。

使用方法:
python demo.py --talker "群名称" --days 0 --api-key "你的Gemini API密钥" --open-browser

参数说明:  （不填则默认从cfg.py读取，更稳定更省事、但不如CLI传参灵活）
--talker: 微信群名称
--days: 获取最近几天的聊天记录 (0表示仅当天，1表示今天和昨天)
--api-key: Gemini API密钥
--open-browser: 生成HTML后自动在浏览器中打开
--start-date: 自定义起始日期 (格式: YYYY-MM-DD)
--end-date: 自定义结束日期 (格式: YYYY-MM-DD)
--output-dir: 指定输出目录 (默认: ./output)
--prompt-path: 自定义Prompt模板路径 (默认: ./prompt_template.txt)

依赖安装:
pip install google-generativeai tqdm requests

作者: AI助手
版本: 1.2
"""

import requests
import os
import subprocess
import time
import argparse
import logging
import json
import sys
import webbrowser
from datetime import datetime, timedelta
import google.generativeai as genai
from pathlib import Path
import tqdm  # 添加tqdm库用于显示进度条
import tkinter as tk
from tkinter import messagebox  # 弹窗，用于提示

# 配置日志
from cfg import CHAT_DEMO_CFG

# 创建日志目录
log_dir = CHAT_DEMO_CFG.get('log_dir', './logs')
os.makedirs(log_dir, exist_ok=True)

# 获取当前时间作为日志文件名
log_filename = f"{log_dir}/error_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log.txt"

# 配置日志
logging.basicConfig(
    level=getattr(logging, CHAT_DEMO_CFG.get('logging_level', 'INFO')),
    format=CHAT_DEMO_CFG.get(
        'logging_format', '%(asctime)s - %(levelname)s - %(message)s'),
    datefmt=CHAT_DEMO_CFG.get('logging_date_format', '%Y-%m-%d %H:%M:%S')
)
logger = logging.getLogger(__name__)

# 添加文件处理器，只记录ERROR级别的日志
file_handler = logging.FileHandler(log_filename, encoding='utf-8')
file_handler.setLevel(logging.ERROR)
file_formatter = logging.Formatter(CHAT_DEMO_CFG.get(
    'logging_format', '%(asctime)s - %(levelname)s - %(message)s'))
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

base_server_ip_port = CHAT_DEMO_CFG.get(
    'chatlog_server_ip_port', "127.0.0.1:5036")
base_server_url = CHAT_DEMO_CFG.get(
    'chatlog_server_url', f"http://{base_server_ip_port}")


def parse_arguments():
    """解析命令行参数"""
    parser = argparse.ArgumentParser(description='微信群聊天记录提取、分析和可视化工具')

    parser.add_argument('--talker', type=str, help='微信群名称')
    parser.add_argument('--days', type=int, default=1,
                        help='获取最近多少天的聊天记录。当填写为0时，代表就只是当天。填写为1时，代表今天和昨天。')
    parser.add_argument('--api-key', type=str, help='Google Gemini API密钥')
    parser.add_argument('--output-dir', type=str,
                        default=CHAT_DEMO_CFG.get('output_dir', './output'), help='输出目录')
    parser.add_argument('--prompt-path', type=str,
                        default=CHAT_DEMO_CFG.get('prompt_template_path', './prompt_template.txt'), help='Prompt模板路径')
    parser.add_argument('--open-browser', action='store_true',
                        help='生成HTML后自动在浏览器中打开')
    parser.add_argument('--start-date', type=str, help='起始日期 (YYYY-MM-DD)')
    parser.add_argument('--end-date', type=str, help='结束日期 (YYYY-MM-DD)')

    return parser.parse_args()


def load_config_from_json():
    return CHAT_DEMO_CFG


def init_gemini_api(api_key):
    """初始化Gemini API"""
    try:
        genai.configure(api_key=api_key)

        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print("可选模型", m.name)

        model = genai.GenerativeModel(
            # gemini-2.5-pro-preview-03-25 available for free (this an update of gemini-2.5-pro-exp-03-25) : r/LocalLLaMA    https://www.reddit.com/r/LocalLLaMA/comments/1jrwstn/gemini25propreview0325_available_for_free_this_an/
            # 'gemini-2.5-pro-preview-03-25'  # 是【gemini-2.5-pro-exp-03-25】的升级版。但是要收费。
            'gemini-2.5-pro-exp-03-25'  # 这个是免费的。
        )
        logger.info("成功连接到Gemini API")
        return model
    except Exception as e:
        logger.error(f"初始化Gemini API失败: {str(e)}")
        print("此为常见问题：根源在海外接口无法联通，请考虑全局proxy上网等选项。")
        raise


wait_sec = CHAT_DEMO_CFG.get('manual_gui_auto_decryption_wait_sec', 30)


def alert_msg():
    """显示阻塞型对话框，并等待用户确认"""
    try:
        print("正在创建提示对话框...")

        # 用于跟踪用户是否正常点击了确认按钮
        user_confirmed = False

        # 创建Tk根窗口
        root = tk.Tk()
        root.title("操作提示")
        # 设置窗口大小和位置
        root.geometry("500x200")
        # 确保窗口在最上层显示
        root.attributes('-topmost', True)

        # 创建对话框内容
        frame = tk.Frame(root, padx=20, pady=20)
        frame.pack(fill=tk.BOTH, expand=True)

        msg_label = tk.Label(
            frame,
            text="因源chatlog项目代码限制（v0.0.15），自动解密功能仅对GUI版本开放。\n\n"
                 "请您在GUI窗口中，点击【开启自动解密】\n"
                 "（如显示【停止自动解密】，说明已处于开启状态，不需要再次点击）",
            wraplength=450,
            justify=tk.LEFT
        )
        msg_label.pack(pady=10)

        # 添加自定义按钮
        def on_close():
            nonlocal user_confirmed
            print("用户点击了确认按钮，对话框即将关闭...")
            user_confirmed = True
            root.destroy()

        ok_button = tk.Button(
            frame,
            text=f"我已处于开启状态，继续\n（后续会等待{wait_sec}秒，等待数据同步完成）",
            width=50,
            height=3,
            command=on_close
        )
        ok_button.pack(pady=10)

        # 处理窗口关闭事件
        def on_window_close():
            nonlocal user_confirmed
            if not user_confirmed:
                print("警告：用户通过右上角关闭了窗口而不是点击确认按钮！")
            root.destroy()

        root.protocol("WM_DELETE_WINDOW", on_window_close)

        # 确保对话框居中显示
        root.update_idletasks()
        width = root.winfo_width()
        height = root.winfo_height()
        x = (root.winfo_screenwidth() // 2) - (width // 2)
        y = (root.winfo_screenheight() // 2) - (height // 2)
        root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

        print("对话框准备完成，开始显示...")
        # 开始主循环
        root.mainloop()
        print("对话框已关闭")

        # 如果用户没有通过按钮确认，而是关闭了窗口，则抛出异常
        if not user_confirmed:
            raise Exception("用户通过关闭窗口取消了操作，程序终止")

    except Exception as e:
        print(f"对话框操作出错: {str(e)}")
        logging.error(f"对话框操作出错: {str(e)}")
        # 重新抛出异常，确保调用者知道操作被取消
        raise Exception(f"对话框操作被取消: {str(e)}")


def run_chatlog_commands():
    """运行chatlog命令启动服务器"""
    try:
        # 从配置中获取chatlog可执行文件路径
        chatlog_exe = CHAT_DEMO_CFG.get(
            'chatlog_exe_path', "D:/Program_Files/ChatLog/chatlog.exe")
        wx_version = CHAT_DEMO_CFG.get('wx_version', "4")

        # 获取微信数据密钥
        logger.info("获取微信数据密钥...")
        key_process = subprocess.run(
            [chatlog_exe, "key"], capture_output=True, text=True, check=True)
        key = key_process.stdout.strip()
        print(key)

        # 解密数据库文件
        logger.info("解密数据库文件...")

        subprocess.run([
            chatlog_exe, "decrypt",
            "--data-dir", CHAT_DEMO_CFG.get('wechat_data_dir'),
            "--key", key,
            "--version", wx_version,
        ], check=True)

        # 如果启用了手动GUI解密选项，则启动GUI并显示阻塞型弹窗
        if CHAT_DEMO_CFG.get('manual_gui_auto_decryption', False):
            # 此处，如果没有新开窗口的话，则需要：——————>（请注意，如无新开窗口，应该在【命令行】 而非PyCharm的【Run运行】中启动，后者会处于等待状态）
            logger.info("正在启动GUI...")

            # 启动GUI程序（在新的终端窗口中）
            if sys.platform == 'win32':
                # 获取完整路径
                chatlog_exe_abs_path = os.path.abspath(chatlog_exe)

                # 确保temp目录存在
                temp_dir = os.path.join(os.path.dirname(__file__), 'temp')
                os.makedirs(temp_dir, exist_ok=True)

                # 创建批处理文件
                # 创建批处理文件临时执行，避免命令行引号嵌套问题
                batch_file = os.path.join(temp_dir, "run_chatlog_temp.bat")
                # batch_file = os.path.join(os.path.dirname(__file__), 'temp', "run_chatlog_temp.bat")

                with open(batch_file, "w") as f:
                    f.write(f'@echo off\n"{chatlog_exe_abs_path}"\npause')
                # 执行批处理文件
                subprocess.Popen(f'start cmd /c "{batch_file}"', shell=True)
            elif sys.platform == 'darwin':  # macOS
                subprocess.Popen(['open', '-a', 'Terminal', chatlog_exe])
            else:  # Linux
                subprocess.Popen(['gnome-terminal', '--', chatlog_exe])

            logger.info("产生一个提示，并阻塞等待交互...")

            # 等待一会儿让GUI程序启动
            time.sleep(0)

            # 显示提示对话框并处理可能的异常
            try:
                logger.info("显示操作提示对话框...")
                alert_msg()
                logger.info("用户确认GUI操作完成")
                # 添加倒计时进度条
                print(f"等待数据同步完成，倒计时 {wait_sec} 秒...")
                with tqdm.tqdm(total=wait_sec, desc="数据同步（同步完后可关闭chatlog的GUI窗口）", unit="秒", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]") as pbar:
                    for _ in range(wait_sec):
                        time.sleep(1)
                        pbar.update(1)
                print("数据同步等待完成")
            except Exception as e:
                logger.error(f"用户取消了操作: {str(e)}")
                raise Exception(f"用户取消了GUI操作，程序终止: {str(e)}")

        # 检查服务器是否已经在运行
        try:
            requests.get(base_server_url + "/api/v1/info", timeout=2)
            logger.info("Chatlog服务器已经在运行")
            return None
        except requests.exceptions.RequestException:
            logger.info("启动新的Chatlog服务器...")

        # 启动HTTP服务器
        server_process = subprocess.Popen([
            chatlog_exe, "server",
            "--addr", base_server_ip_port,
            "--data-dir", CHAT_DEMO_CFG.get('wechat_data_dir'),
            "--work-dir", CHAT_DEMO_CFG.get('chatlog_work_dir'),
            "--platform", "windows",
            "--version", wx_version,
        ])

        # 等待服务器启动
        logger.info("等待服务器启动...")

        def wait_for_server_startup():
            """等待服务器启动并确认可以访问"""
            max_retries = 10
            retry_interval = 1
            for i in range(max_retries):
                try:
                    response = requests.get(
                        base_server_url + "/api/v1/chatroom", timeout=2)
                    if response.status_code == 200 and response.text:
                        logger.info("服务器启动成功，已确认可以访问聊天室数据")
                        return
                    else:
                        logger.warning(
                            f"服务器响应但未返回数据，等待重试 ({i + 1}/{max_retries})...")
                except requests.exceptions.RequestException:
                    logger.info(f"等待服务器启动中 ({i + 1}/{max_retries})...")
                time.sleep(retry_interval)

            # 多次重试后仍未成功启动，抛出异常
            raise Exception("服务器启动失败，无法访问聊天室数据")

        wait_for_server_startup()
        return server_process
    except Exception as e:
        logger.error(f"运行chatlog命令失败: {str(e)}")
        raise


def get_chat_logs(talker_name, start_date=None, end_date=None, days=7):
    """获取指定群的聊天记录"""
    try:
        # 计算日期范围
        if end_date is None:
            # 设置为当前日期
            end_date_obj = datetime.now()
            end_date_obj = end_date_obj + timedelta(
                # 之前以为的Bug：加1天以符合左闭右开区间——————>后来发现，应该是【3.x】没获得数据，仅此而已。
                # days=1
                days=0
            )
            end_date = end_date_obj.strftime("%Y-%m-%d")
        else:
            end_date_obj = datetime.strptime(end_date, "%Y-%m-%d") + timedelta(
                # days=1             # 如果end_date已提供，也需要加1天
                days=0  # 后来发现，0天就行。并不是这个的bug。
            )
            end_date = end_date_obj.strftime("%Y-%m-%d")

        if start_date is None:
            start_date = (datetime.now() - timedelta(days=days)
                          ).strftime("%Y-%m-%d")

        logger.info(f"获取群'{talker_name}'从{start_date}到{end_date}的聊天记录...")

        # URL编码群名称
        encoded_talker_name = requests.utils.quote(talker_name)

        # 构建API URL
        url = f"{base_server_url}/api/v1/chatlog?time={start_date}~{end_date}&talker={encoded_talker_name}"

        # 发送GET请求
        response = requests.get(url, timeout=30)

        if response.status_code == 200:
            chat_logs = response.text
            if not chat_logs:
                logger.warning("获取到的聊天记录为空。可能是群不存在或在指定时间范围内没有消息。")
            else:
                logger.info(f"成功获取聊天记录: {len(chat_logs)}字符")
            return chat_logs
        else:
            error_msg = f"获取聊天记录失败: {response.status_code}, {response.text}"
            logger.error(error_msg)
            raise Exception(error_msg)
    except Exception as e:
        logger.error(f"获取聊天记录时出错: {str(e)}")
        raise


def read_prompt_template(template_path):
    """读取Prompt模板文件"""
    try:
        logger.info(f"从{template_path}读取prompt模板")
        with open(template_path, 'r', encoding='utf-8') as file:
            template = file.read()

        if not template:
            raise ValueError("Prompt模板文件为空")

        logger.info(f"成功读取prompt模板: {len(template)}字符")
        return template
    except Exception as e:
        logger.error(f"读取prompt模板失败: {str(e)}")
        raise


def build_complete_prompt(prompt_template, chat_logs, talker):
    """构建发送给Gemini的完整Prompt"""
    logger.info("构建完整prompt...")

    if not chat_logs:
        raise ValueError("聊天记录为空，无法构建prompt")

    complete_prompt = f"""你好，此处的txt为我的【群日报生成要求prompt】，另一外一份txt为我的【群聊记录】。

请你根据最新的群聊记录，按照prompt要求，生成一份群日报。要求仅返回html，不要返回其他内容。

【群聊名称】：
{talker}

【群日报生成要求prompt】：
{prompt_template}

【群聊记录】：
{chat_logs}

谢谢"""
    logger.info(f"完整prompt已构建: {len(complete_prompt)}字符")
    return complete_prompt


def extract_html_from_response(response_text):
    """从Gemini API的响应文本中提取HTML内容"""
    # 如果已经是HTML，直接返回
    if response_text.strip().startswith('<'):
        return response_text

    # 尝试从代码块中提取HTML
    if '```html' in response_text and '```' in response_text.split('```html', 1)[1]:
        html_content = response_text.split(
            '```html', 1)[1].split('```', 1)[0].strip()
        return html_content

    # 尝试提取<html>标签内容
    if '<html' in response_text and '</html>' in response_text:
        start_idx = response_text.find('<html')
        end_idx = response_text.find('</html>') + 7
        html_content = response_text[start_idx:end_idx]
        return html_content

    # 如果无法提取HTML，记录警告并返回原始文本
    logger.warning("无法从响应中提取HTML，返回原始文本")
    return response_text


def generate_html_with_gemini(model, prompt):
    """使用Gemini API生成HTML内容"""
    try:
        print("""
调试1 （有时会卡在这里，丢失后续的 logger.info 输出？）
        经过分析，应该是【flush缓冲区】、以及【print 和 logger.info】的乱序问题（这个倒经常出现）
                一般来说，稍微等待一会儿，即可""".strip())
        sys.stdout.flush()
        logger.info("向Gemini API发送prompt...")
        sys.stdout.flush()
        # 设置生成参数
        generation_config = {
            "temperature": 0.7,
            "top_p": 0.8,
            "top_k": 40,
            # "max_output_tokens": 8192,
            "max_output_tokens": 65536,
        }

        # 发送请求到Gemini
        response = model.generate_content(
            prompt,
            generation_config=generation_config,
            stream=True,  # 流式传输
        )

        # 处理流式响应
        print("正在生成日报内容，请稍候...")
        sys.stdout.flush()
        response_text = ""
        # 创建一个动态进度条
        progress_bar = tqdm.tqdm(desc="生成进度", unit="字符", dynamic_ncols=True)

        for chunk in response:
            if hasattr(chunk, 'text') and chunk.text:
                current_chunk = chunk.text
                response_text += current_chunk
                # 更新进度条
                progress_bar.update(len(current_chunk))
                # 可选：每接收到一个块后显示最新的少量文本
                if len(current_chunk) > 0 and len(current_chunk) < 100:
                    # 显示最近添加的文本片段，但避免输出HTML标签
                    readable_chunk = current_chunk.replace(
                        '<', '＜').replace('>', '＞')
                    progress_bar.set_description(
                        f"最新内容: {readable_chunk[:30]}...")

        # 关闭进度条
        progress_bar.close()
        print(f"内容生成完毕！共 {len(response_text)} 个字符")
        sys.stdout.flush()

        # 提取HTML内容
        html_content = extract_html_from_response(response_text)

        # 验证HTML基本结构
        if not ('<html' in html_content.lower() and '</html>' in html_content.lower()):
            logger.warning("生成的内容可能不是有效的HTML")

        logger.info(f"成功生成HTML内容: {len(html_content)}字符")
        return html_content
    except Exception as e:
        logger.error(f"使用Gemini生成HTML失败: {str(e)}")
        raise


def save_html(html_content, output_dir, talker_name):
    """保存HTML文件"""
    try:
        # 确保输出目录存在
        os.makedirs(output_dir, exist_ok=True)

        # 创建文件名，包含日期和时间
        current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{talker_name}_群日报_{current_datetime}.html"
        filepath = os.path.join(output_dir, filename)

        logger.info(f"保存HTML至: {filepath}")

        # 写入HTML文件
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(html_content)

        logger.info(f"成功保存HTML文件: {filepath}")
        return filepath
    except Exception as e:
        logger.error(f"保存HTML文件失败: {str(e)}")
        raise


def open_in_browser(html_filepath):
    """在默认浏览器中打开HTML文件"""
    try:
        logger.info(f"在浏览器中打开HTML文件: {html_filepath}")
        webbrowser.open(f"file://{os.path.abspath(html_filepath)}")
    except Exception as e:
        logger.error(f"在浏览器中打开文件失败: {str(e)}")


def main():
    """主函数"""
    server_process = None

    try:
        # 解析命令行参数
        args = parse_arguments()

        print("-" * 50)
        print("🚀 微信群聊日报生成工具已启动")

        # 尝试从配置文件加载配置
        config = load_config_from_json()

        # 获取talkers列表
        talkers = []
        if args.talker:
            talkers = [args.talker]
        elif 'talkers' in config and isinstance(config['talkers'], list):
            talkers = config['talkers']
            logger.info(f"从配置文件加载talkers: {talkers}")

        if not talkers:
            raise ValueError(
                "必须提供至少一个talker名称，可通过--talker参数或在cfg.json中设置talkers数组")

        print(f"📊 目标群聊: {', '.join(talkers)}")
        if args.start_date and args.end_date:
            print(f"📅 时间范围: {args.start_date} 至 {args.end_date}")
        else:
            print(f"📅 时间范围: 近 {args.days} 天")
        print("-" * 50)

        # 检查API密钥
        if not args.api_key:
            args.api_key = config.get(
                'api_key') or os.environ.get('GEMINI_API_KEY')
            if not args.api_key:
                raise ValueError(
                    "必须提供Gemini API密钥，可通过--api-key参数、cfg.py配置文件或GEMINI_API_KEY环境变量设置")

        print("⏳ 启动数据服务中...")
        # 运行chatlog命令
        server_process = run_chatlog_commands()
        print("✅ 数据服务已启动")

        # 初始化Gemini API
        print("⏳ 连接AI服务中...")
        model = init_gemini_api(args.api_key)
        print("✅ AI服务连接成功")

        # 读取Prompt模板
        print("⏳ 正在加载日报模板...")
        prompt_template = read_prompt_template(args.prompt_path)
        print("✅ 模板加载完成")

        # 处理每个talker
        for talker in talkers:
            try:
                print(f"\n--- 开始处理 「{talker}」 ---")

                # 获取聊天记录
                print(f"⏳ 正在获取「{talker}」的聊天记录...")
                chat_logs = get_chat_logs(
                    talker,
                    args.start_date,
                    args.end_date,
                    args.days
                )

                # 如果没有获取到聊天记录，继续下一个
                if not chat_logs:
                    print(f"❌ 未获取到「{talker}」的聊天记录，请检查群名称是否正确或时间范围内是否有消息")
                    logger.error(f"未获取到「{talker}」的聊天记录，跳过。")
                    continue

                print(f"✅ 成功获取聊天记录: {len(chat_logs)}字符")

                # 构建完整的Prompt
                print("⏳ 正在准备AI分析数据...")
                complete_prompt = build_complete_prompt(
                    prompt_template, chat_logs,
                    talker=talker,
                )
                print("✅ 分析数据准备完成")

                # 使用Gemini生成HTML
                print("⏳ 开始AI分析并生成日报...")
                html_content = generate_html_with_gemini(
                    model, complete_prompt)

                # 保存HTML文件
                print("⏳ 正在保存日报文件...")
                html_filepath = save_html(
                    html_content, args.output_dir, talker)
                print(f"✅ 日报已保存至: {html_filepath}")

                # 如果指定了，在浏览器中打开HTML文件
                if CHAT_DEMO_CFG.get('auto_open_browser', False):
                    print("⏳ 正在打开浏览器...")
                    open_in_browser(html_filepath)
                    print("✅ 已在浏览器中打开日报")

                print(f"--- 「{talker}」处理完成 ---")

            except Exception as e:
                print(f"\n❌ 处理「{talker}」时出错: {str(e)}")
                logger.error(f"处理「{talker}」时出错: {str(e)}")
                continue

        print("-" * 50)
        print("🎉 所有任务处理完成！")
        print("-" * 50)

    except KeyboardInterrupt:
        print("\n❌ 用户中断处理")
        logger.info("用户中断处理")
    except Exception as e:
        print(f"\n❌ 处理出错: {str(e)}")
        logger.error(f"主程序处理过程中出错: {str(e)}")
        sys.exit(1)

    finally:
        # 确保关闭chatlog服务器，如果是我们启动的
        if server_process:
            print("⏳ 正在关闭数据服务...")
            server_process.terminate()
            print("✅ 数据服务已关闭")
            logger.info("Chatlog服务器已终止。")

        # 在程序结束时，如果有错误发生，打开错误日志文件
        if os.path.exists(log_filename) and os.path.getsize(log_filename) > 0:
            print(f"\n⚠️ 程序运行过程中发生了错误，错误日志已保存至: {log_filename}")
            log_path = os.path.join(os.path.dirname(__file__), log_filename)
            try:
                # 尝试在默认文本编辑器中打开日志文件
                if sys.platform == 'win32':
                    os.startfile(log_path)
                elif sys.platform == 'darwin':  # macOS
                    subprocess.call(['open', log_path])
                else:  # Linux
                    subprocess.call(['xdg-open', log_path])
                print("✅ 已打开错误日志文件")
            except Exception as e:
                print(f"❌ 打开错误日志文件失败: {str(e)}")
                print(f"请手动打开错误日志文件查看: {log_path}")


if __name__ == "__main__":
    main()
