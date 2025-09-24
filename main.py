from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.logger import Logger
from datetime import datetime
import threading
import json
import time
import requests
import os
import numpy as np
from io import BytesIO

# 设置中文字体支持
Window.clearcolor = (0.95, 0.95, 0.95, 1)  # 设置背景色为浅灰色

# 全局变量
max_roll_in_rate = None
stop_rate_query = False
alert_threshold = None

class TextRedirector:
    """将输出重定向到Kivy文本控件"""
    def __init__(self, text_widget):
        self.text_widget = text_widget
    
    def write(self, string):
        self.text_widget.text += string
        # 滚动到底部
        self.text_widget.cursor = (len(self.text_widget.text), 0)
        self.text_widget.scroll_y = 0
    
    def flush(self):
        pass

class ServerToolLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(ServerToolLayout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10
        self.padding = 10
        
        # 创建标题标签
        title_label = Label(text='服务器工具', font_size=24, bold=True, size_hint_y=None, height=50)
        self.add_widget(title_label)
        
        # 创建日志显示区域
        self.log_text = TextInput(readonly=True, font_size=14, multiline=True, size_hint_y=1)
        scroll_log = ScrollView(size_hint_y=1)
        scroll_log.add_widget(self.log_text)
        self.add_widget(scroll_log)
        
        # 创建阈值设置区域
        threshold_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=40)
        self.threshold_entry = TextInput(text='', hint_text='输入声音提示阈值', multiline=False, font_size=14)
        threshold_box.add_widget(self.threshold_entry)
        self.set_threshold_btn = Button(text='设置阈值', font_size=14, size_hint_x=0.3)
        self.set_threshold_btn.bind(on_press=self.set_threshold)
        threshold_box.add_widget(self.set_threshold_btn)
        self.add_widget(threshold_box)
        
        # 创建按钮区域
        button_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
        self.get_time_btn = Button(text='获取服务器时间', font_size=14)
        self.get_time_btn.bind(on_press=self.start_get_time_thread)
        button_box.add_widget(self.get_time_btn)
        
        self.get_rate_btn = Button(text='获取汇率信息', font_size=14)
        self.get_rate_btn.bind(on_press=self.toggle_rate_query)
        button_box.add_widget(self.get_rate_btn)
        
        self.exit_btn = Button(text='退出', font_size=14)
        self.exit_btn.bind(on_press=App.get_running_app().stop)
        button_box.add_widget(self.exit_btn)
        self.add_widget(button_box)
        
        # 将标准输出重定向到日志区域
        import sys
        sys.stdout = TextRedirector(self.log_text)
        
        print("服务器工具已启动")
        print("点击'获取服务器时间'按钮开始获取时间数据")
        print("点击'获取汇率信息'按钮开始获取汇率数据")
        print("所有操作日志和错误信息将显示在此窗口中")
    
    def set_threshold(self, instance):
        global alert_threshold
        threshold_text = self.threshold_entry.text.strip()
        
        if not threshold_text:
            alert_threshold = None
            print("[提示] 声音提示阈值已清除，现在将对所有新高值播放声音")
            return
        
        try:
            threshold_value = float(threshold_text)
            alert_threshold = threshold_value
            print(f"[提示] 声音提示阈值已设置为: {threshold_value}")
        except ValueError:
            print("[错误] 无效的阈值，请输入数字")
    
    def start_get_time_thread(self, instance):
        thread = threading.Thread(target=self.get_time_thread, daemon=True)
        thread.start()
    
    def toggle_rate_query(self, instance):
        global stop_rate_query
        if not stop_rate_query:
            # 开始查询
            thread = threading.Thread(target=self.get_rate_thread, daemon=True)
            thread.start()
        else:
            # 停止查询
            stop_rate_query = False
            print("准备重新开始查询...")
    
    def get_time_thread(self):
        # 更新时间戳
        current_datetime = datetime.now().strftime('%Y%m%d%H%M%S')
        
        print("\n=== 开始获取服务器时间 ===")
        server_time = self.get_now_time(current_datetime)
        if server_time:
            print(f"测试结果: 成功获取服务器时间 - {server_time}")
        else:
            print("测试结果: 获取服务器时间失败")
    
    def get_rate_thread(self):
        global max_roll_in_rate, stop_rate_query
        stop_rate_query = False  # 重置停止标志
        print("\n=== 开始循环获取汇率信息（每秒一次）===")
        print("点击'获取汇率信息'按钮可停止循环查询")
        
        while not stop_rate_query:
            rate_info = self.get_conversion_rate()
            if rate_info is None:
                print("[提示] 无法获取汇率信息")
            else:
                self.process_rate_info(rate_info)
            
            # 等待1秒
            time.sleep(1)
            
            # 检查是否需要停止循环
            if stop_rate_query:
                print("循环查询已停止")
                break
    
    def play_notification_sound(self):
        try:
            # 在Android上，我们使用更简单的声音播放方式
            # Kivy的SoundLoader可以加载简单的音频文件
            # 这里我们创建一个简单的音频数据并播放
            sample_rate = 44100
            duration = 1  # 缩短声音时长以适应移动设备
            
            # 生成简单的正弦波
            t = np.linspace(0, duration, int(sample_rate * duration), False)
            freq = 440  # A4音
            tone = np.sin(freq * 2 * np.pi * t)
            
            # 转换为16位整数
            tone = np.int16(tone * 32767)
            
            # 将音频数据保存到临时文件
            temp_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "temp_sound.wav")
            
            # 使用简单的WAV格式头部
            # 注意：这是一个简化的实现，可能需要根据实际情况调整
            try:
                import wave
                with wave.open(temp_file, 'wb') as wf:
                    wf.setnchannels(1)
                    wf.setsampwidth(2)
                    wf.setframerate(sample_rate)
                    wf.writeframes(tone.tobytes())
                
                # 加载并播放声音
                sound = SoundLoader.load(temp_file)
                if sound:
                    sound.play()
                
                # 播放后删除临时文件
                # 延迟删除以确保文件已被播放
                Clock.schedule_once(lambda dt: self.remove_temp_file(temp_file), duration + 0.5)
            except Exception as e:
                print(f"[警告] 无法创建临时声音文件: {e}")
        except Exception as e:
            print(f"[警告] 播放声音时出错: {e}")
    
    def remove_temp_file(self, file_path):
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f"[警告] 无法删除临时文件: {e}")
    
    def get_conversion_rate(self):
        """获取汇率信息"""
        url = "https://qjd67cc.nowkk.com/v1/user/wallet/getConvertRate"
        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-encoding": "gzip, deflate",
            "accept-language": "zh-CN,zh;q=0.9",
            "appdevice": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
            "apptype": "1",
            "clienttype": "3",
            "clientversion": "4.3.1",
            "deviceid": "8E951CBADE4601929FCA0226B4625882",
            "language": "zh_CN",
            "priority": "u=1, i",
            "referer": "https://qjd67cc.nowkk.com/MainPage/SwapPage3",
            "sec-ch-ua": "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\", \"Google Chrome\";v=\"132\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "supportwebp": "true",
            "token": "b4e5813dbdf8df0d1758701052a8c8559bcd9a948f",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
            "version": "v1",
            "x-request-id": "5bab65fc-980d-4307-a28b-916ebd8134fc"
        }
        
        try:
            response = requests.get(url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                try:
                    # 尝试直接解析JSON响应
                    result = response.json()
                    return result
                except json.JSONDecodeError as e:
                    print(f"[错误] JSON解析失败: {e}")
                    return None
                except Exception as e:
                    print(f"[错误] 处理响应数据时出错: {e}")
                    return None
            else:
                print(f"[错误] 请求失败，状态码: {response.status_code}")
                return None
        except Exception as e:
            print(f"[错误] 无法获取汇率信息: {e}")
            return None
    
    def get_now_time(self, current_datetime):
        """获取服务器当前时间"""
        try:
            print(f"开始获取服务器时间...")
            
            # 构建请求URL
            url = f"https://m518.mos077.com/transform.php?ver={current_datetime}"
            print(f"请求URL: {url}")
            # 请求载荷
            payload = {
                "p": "service_mainget",
                "ver": current_datetime,
                "": "",
                "langx": "zh-cn",
                "login": "N",
            }
            
            # 请求头
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Content-Type": "application/x-www-form-urlencoded",
                "Referer": "https://m518.mos077.com/",
                "Accept": "*/*",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive",
                "X-Requested-With": "XMLHttpRequest"
            }
            
            # 发送POST请求
            response = requests.post(url, data=payload, headers=headers, timeout=10)
            
            if response.status_code == 200:
                print(f"[成功] 服务器响应成功，状态码: {response.status_code}")
                
                try:
                    # 解析XML响应
                    import xml.etree.ElementTree as ET
                    root = ET.fromstring(response.text)
                    
                    # 查找now_time元素
                    now_time_element = root.find('.//now_time')
                    if now_time_element is not None and now_time_element.text:
                        now_time = now_time_element.text.strip()
                        print(f"[成功] 获取到服务器时间: {now_time}")
                        return now_time
                    else:
                        error_msg = "[失败] XML中未找到now_time元素"
                        print(error_msg)
                        return None
                except ET.ParseError as e:
                    error_msg = f"[错误] XML解析失败: {e}"
                    print(error_msg)
                    return None
            else:
                error_msg = f"[错误] HTTP请求失败，状态码: {response.status_code}"
                print(error_msg)
                return None
        except Exception as e:
            error_msg = f"[异常] 获取服务器时间异常: {e}"
            print(error_msg)
            return None
    
    def process_rate_info(self, rate_info):
        global max_roll_in_rate
        try:
            # 解析rollInRate数值
            if isinstance(rate_info, dict):
                if 'rollInRate' in rate_info:
                    self._process_roll_in_rate(rate_info['rollInRate'])
                else:
                    # 尝试查找嵌套的rollInRate字段
                    roll_in_rate = self.find_roll_in_rate(rate_info)
                    if roll_in_rate is not None:
                        self._process_roll_in_rate(roll_in_rate)
                    else:
                        print("[错误] 汇率信息中未找到rollInRate字段")
            else:
                print(f"[错误] 汇率信息格式不正确: {type(rate_info)}")
        except Exception as e:
            print(f"[错误] 解析rollInRate时出现异常: {e}")
    
    def _process_roll_in_rate(self, roll_in_rate):
        global max_roll_in_rate, alert_threshold
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        try:
            numeric_rate = float(roll_in_rate)
            is_new_max = False
            
            if max_roll_in_rate is None:
                max_roll_in_rate = numeric_rate
                is_new_max = True
            elif numeric_rate > max_roll_in_rate:
                max_roll_in_rate = numeric_rate
                is_new_max = True
            
            if is_new_max:
                print(f"[{current_time}] [成功] 提取到rollInRate数值: {roll_in_rate} (新高！)")
            
            # 检查是否达到声音提示阈值（无论是否为新高值）
            should_play_sound = False
            if alert_threshold is not None:
                if numeric_rate >= alert_threshold:
                    should_play_sound = True
                    print(f"[{current_time}] [提醒] rollInRate数值 {roll_in_rate} 大于等于设置的阈值 {alert_threshold}！")
            else:
                # 如果没有设置阈值，只在新高值时播放声音
                should_play_sound = is_new_max
            
            if should_play_sound:
                # 在主线程中播放声音
                Clock.schedule_once(lambda dt: self.play_notification_sound())
        except ValueError:
            # 如果无法转换为数字，不打印输出
            pass
    
    def find_roll_in_rate(self, data):
        """递归查找嵌套字典中的rollInRate字段"""
        if isinstance(data, dict):
            if 'rollInRate' in data:
                return data['rollInRate']
            for key, value in data.items():
                result = self.find_roll_in_rate(value)
                if result is not None:
                    return result
        elif isinstance(data, list):
            for item in data:
                result = self.find_roll_in_rate(item)
                if result is not None:
                    return result
        return None

class ServerToolApp(App):
    def build(self):
        return ServerToolLayout()

if __name__ == '__main__':
    ServerToolApp().run()