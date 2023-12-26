import cv2
import numpy as np

# GStreamer pipeline for capturing video from a UDP stream with videoscale
cap = cv2.VideoCapture("udpsrc port=5600 ! application/x-rtp, payload=96 ! rtph264depay ! avdec_h264 ! videoconvert ! videoscale ! video/x-raw, width=640, height=480 ! appsink")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("UDP Video Stream", frame)
    key = cv2.waitKey(30) & 0xff
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
