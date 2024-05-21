import cv2
import numpy as np
from ultralytics import YOLO
import random
import time

# Load the YOLOv8 model
model = YOLO('yolov8n.pt')

# Replace with your IP Webcam RTSP URL
rtsp_url = 'rtsp://192.168.100.104:8080/h264_ulaw.sdp'

# Capture the video stream
cap = cv2.VideoCapture(rtsp_url)

# Function to generate a random color avoiding shades of red
def get_random_color():
    while True:
        color = tuple(random.randint(0, 255) for _ in range(3))
        if color[2] < 100:  # Avoid shades of red
            break
    return color

# Store colors for each detected person
colors = {}
person_boxes = {}
selected_person = None
start_time = None

def on_mouse(event, x, y, flags, param):
    global selected_person, start_time
    if event == cv2.EVENT_LBUTTONDOWN:
        for person_id, box in person_boxes.items():
            x1, y1, x2, y2 = box
            if x1 <= x <= x2 and y1 <= y <= y2:
                if selected_person == person_id:
                    selected_person = None
                    start_time = None
                else:
                    selected_person = person_id
                    start_time = time.time()

cv2.namedWindow('RTSP Stream', cv2.WINDOW_NORMAL)
cv2.setMouseCallback('RTSP Stream', on_mouse)

# Set desired window size to fit your screen
desired_width = 640
desired_height = 480
cv2.resizeWindow('RTSP Stream', desired_width, desired_height)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Resize frame for processing and display
    frame_resized = cv2.resize(frame, (desired_width, desired_height))

    # Perform object detection
    results = model(frame_resized)[0]  # Updated to handle list format

    # Draw bounding boxes for each detected person
    person_boxes.clear()
    for i, box in enumerate(results.boxes):  # Updated to iterate over boxes
        x1, y1, x2, y2 = map(int, box.xyxy[0].cpu().numpy())
        conf, cls = box.conf.item(), box.cls.item()
        if cls == 0:  # Class 0 corresponds to 'person' in COCO dataset
            if i not in colors:
                colors[i] = get_random_color()
            color = colors[i]
            if i == selected_person:
                color = (0, 0, 255)  # Red color for selected person
            cv2.rectangle(frame_resized, (x1, y1), (x2, y2), color, 2)
            person_boxes[i] = (x1, y1, x2, y2)

    # Display timer for selected person
    if selected_person is not None and start_time is not None:
        elapsed_time = int(time.time() - start_time)
        cv2.putText(frame_resized, f'Time: {elapsed_time}s', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('RTSP Stream', frame_resized)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
