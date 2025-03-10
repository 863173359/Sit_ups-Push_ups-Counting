import cv2

def video_capture():
    # 打开摄像头
    cap = cv2.VideoCapture(0)

    # 检查摄像头是否成功打开
    if not cap.isOpened():
        print("Error: Could not open camera.")
        exit()

    # 获取摄像头的默认帧大小
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    # 设置视频保存相关参数
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 使用MP4V编解码器
    out = None
    recording = False

    # 创建窗口
    cv2.namedWindow("Camera Feed", cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("Camera Feed", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    while True:
        # 读取帧
        ret, frame = cap.read()

        # 检查帧是否成功读取
        if not ret:
            print("Error: Could not read frame.")
            break

        # 显示帧
        cv2.imshow("Camera Feed", frame)

        # 检测按键
        key = cv2.waitKey(1)

        # 如果按下 's' 键，切换录制状态
        if key == ord('s'):
            recording = not recording
            if recording:
                print("Recording started. Press 's' again to stop.")
                video_name = 'output.mp4'
                out = cv2.VideoWriter(video_name, fourcc, 20.0, (frame_width, frame_height))
            else:
                print("Recording stopped.")
                if out is not None:
                    out.release()
                    out = None

        # 检测按键，如果按下 'q' 键，退出循环
        elif key == ord('q'):
            break

        # 如果正在录制，将帧写入输出视频文件
        if recording and out is not None:
            out.write(frame)

    # 释放摄像头和视频写入对象的资源
    cap.release()
    if out is not None:
        out.release()

    # 关闭窗口
    cv2.destroyAllWindows()

if __name__ == '__main__':
    video_capture()
