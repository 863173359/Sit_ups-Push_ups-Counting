import cv2


def Video_show(video_file="output.mp4"):
    # Get the video file name from the user
    video_file = video_file

    # Open the video file
    cap = cv2.VideoCapture(video_file)

    # Check if the video file is successfully opened
    if not cap.isOpened():
        print("Error: Could not open video file.")
        exit()

    # Get the video's frame width and height
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    # Create a window
    cv2.namedWindow("Video Player", cv2.WINDOW_NORMAL)

    # Set the window to fullscreen
    cv2.setWindowProperty("Video Player", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    while True:
        # Read a frame from the video
        ret, frame = cap.read()

        # Check if the frame is successfully read
        if not ret:
            print("End of video.")
            break

        # Display the frame
        cv2.imshow("Video Player", frame)

        # Check for the 'q' key to exit the loop
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    Video_show()