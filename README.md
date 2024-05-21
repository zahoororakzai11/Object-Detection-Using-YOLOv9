This task involves creating a real-time object detection system using a Python script with OpenCV and other necessary libraries. The system will fetch an RTSP video stream from a mobile camera and perform object detection using the YOLOv8 model to detect multiple people in the stream, assigning unique colors to their bounding boxes and allowing user interaction to change the color of these boxes.

Hardware Required
Laptop/PC: Capable of running object detection models.
Mobile phone with Android OS: To generate the RTSP video stream using the IP Webcam app or any other RTSP video streaming camera.
Software Requirements
Python Script: Developed using OpenCV and other necessary libraries.
Detailed Task Steps
RTSP Video Stream:

Fetch an RTSP video stream generated from the mobile camera using the IP Webcam app on Android or any other RTSP video streaming camera for convenience.
Object Detection:

Implement YOLOv8 object detection on the live RTSP video stream.
Detect multiple people in the stream and draw bounding boxes around them.
Bounding Box Specifications:

Assign unique, randomly generated colors to each bounding box, avoiding shades of red.
Ensure each detected person has a different colored bounding box.
User Interaction:

Display the video in an OpenCV window.
Allow users to click on a bounding box to change its color to red.
Once a box is red, display a timer starting from 0 seconds at the top of the display window.
The box of the selected person should stay red even if the detection loses him for a few moments by using a tracker.
If a user selects another person, the previous person’s box should revert to a random color, and the new person’s box should turn red with the timer reset to 0 seconds.
By following these steps, you will develop an interactive object detection system that can detect multiple people in a live video stream, assign unique colors to their bounding boxes, and allow user interaction to track and highlight individuals.
