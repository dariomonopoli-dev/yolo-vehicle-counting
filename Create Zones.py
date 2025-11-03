import cv2
import numpy as np

polygon_points = []

video_path = 'assets/video.mp4'
cap = cv2.VideoCapture(video_path)


def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Point Added: (X: {x}, Y: {y})")



while True:
    # Capture the first frame
    ret, frame = cap.read()
    frame = cv2.resize(frame, (1920, 1080))
    # Create a window and set the mouse callback
    cv2.namedWindow('Frame')
    cv2.setMouseCallback('Frame', mouse_callback)

    # Draw the polygon on the frame
    cv2.imshow('Frame', frame)

    # Press 'Esc' to exit
    key = cv2.waitKey(0)
    if key == 27:
        break

cv2.destroyAllWindows()
cap.release()
