import cv2
from imread_from_url import imread_from_url

from yolov10 import YOLOv10, draw_detections

# Initialize yolov8 object detector
model_path = "models/yolov10l.onnx"
detector = YOLOv10(model_path, conf_thres=0.2)

# Read image
img_url = "https://github.com/ibaiGorordo/ONNX-YOLOv10-Object-Detection/blob/assets/assets/test.png?raw=true"
img = imread_from_url(img_url)

# Detect Objects
class_ids, boxes, confidences = detector(img)

# Draw detections
combined_img = draw_detections(img, boxes, confidences, class_ids)
cv2.namedWindow("Detected Objects", cv2.WINDOW_NORMAL)
cv2.imshow("Detected Objects", combined_img)
cv2.waitKey(0)
