import cv2

from yolov10 import YOLOv10, draw_detections

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Initialize object detector
model_path = "models/yolov10s.onnx"
detector = YOLOv10(model_path, conf_thres=0.5)

cv2.namedWindow("Detected Objects", cv2.WINDOW_NORMAL)
while cap.isOpened():

    # Read frame from the video
    ret, frame = cap.read()

    if not ret:
        break

    # Detect objects
    class_ids, boxes, confidences = detector(frame)

    combined_img = draw_detections(frame, boxes, confidences, class_ids)
    cv2.imshow("Detected Objects", combined_img)

    # Press key q to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
