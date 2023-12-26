import cv2

# GStreamer pipeline for capturing video from a UDP stream with reduced resolution
cap = cv2.VideoCapture("udpsrc port=5600 ! application/x-rtp, payload=96 ! rtph264depay ! avdec_h264 ! videoscale ! videoconvert ! appsink")

# Set the desired width and height for the reduced resolution
desired_width = 1280
desired_height = 720

# Set the caps filter to specify the desired resolution
caps_filter = f"video/x-raw,width={desired_width},height={desired_height}"

# Append the caps filter to the pipeline
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"H264"))
cap.set(cv2.CAP_PROP_FPS, 30)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, desired_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, desired_height)

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
