#test777
import cv2
import numpy as np

# GStreamer pipeline for capturing video from a UDP stream
cap = cv2.VideoCapture("udpsrc port=5600 ! application/x-rtp, payload=96 ! rtph264depay ! avdec_h264 ! videoconvert ! appsink")

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