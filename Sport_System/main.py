import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import Pushup
import Pushup_intime
import Situps
import Situp_intime
import Video_Capture
import Video_show

def get_video_path():
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口

    file_path = filedialog.askopenfilename(title="选择视频文件", filetypes=[("视频文件", "*.mp4;*.avi;*.mkv")])

    return file_path

def run_pushup_video_detection():
    video_path = get_video_path()
    if video_path:
        count = Pushup.Pushup(video_path)
        result_label.config(text=f"俯卧撑计数: {count}")

def run_pushup_realtime_detection():
    count = Pushup_intime.Pushup_intime()
    result_label.config(text=f"俯卧撑实时检测计数: {count}")

def run_situp_video_detection():
    video_path = get_video_path()
    if video_path:
        count = Situps.Situp(video_path)
        result_label.config(text=f"仰卧起坐计数: {count}")

def run_situp_realtime_detection():
    count = Situp_intime.Situp_intime()
    result_label.config(text=f"仰卧起坐实时检测计数: {count}")

def run_video_capture():
    Video_Capture.video_capture()
    result_label.config(text="视频捕获完成")

def run_video_show():
    video_path = get_video_path()
    Video_show.Video_show(video_path)
    result_label.config(text="视频展示完成")

def exit_program():
    if messagebox.askokcancel("退出", "确定退出系统吗？"):
        root.destroy()

# 创建主窗口
root = tk.Tk()
root.title("运动检测系统")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))  # 设置窗口全屏

# 添加样式
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 16), padding=10)
style.configure("TLabel", font=("Helvetica", 18), padding=10)

# 添加按钮
pushup_video_button = ttk.Button(root, text="俯卧撑视频检测", command=run_pushup_video_detection)
pushup_video_button.pack(pady=20)

pushup_realtime_button = ttk.Button(root, text="俯卧撑实时检测", command=run_pushup_realtime_detection)
pushup_realtime_button.pack(pady=20)

situp_video_button = ttk.Button(root, text="仰卧起坐视频检测", command=run_situp_video_detection)
situp_video_button.pack(pady=20)

situp_realtime_button = ttk.Button(root, text="仰卧起坐实时检测", command=run_situp_realtime_detection)
situp_realtime_button.pack(pady=20)

video_capture_button = ttk.Button(root, text="视频捕获", command=run_video_capture)
video_capture_button.pack(pady=20)

video_show_button = ttk.Button(root, text="视频展示", command=run_video_show)
video_show_button.pack(pady=20)

exit_button = ttk.Button(root, text="退出", command=exit_program)
exit_button.pack(pady=20)

# 显示结果的标签
result_label = ttk.Label(root, text="")
result_label.pack(pady=20)

# 启动主循环
root.mainloop()

