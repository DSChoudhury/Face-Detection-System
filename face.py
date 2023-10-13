#real Time
import torch
import cv2
import numpy as np
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
cap = cv2.VideoCapture("")
while cap.isOpened():
    ret, frame = cap.read()
    
    # Make detections 
    results = model(frame)
    
    cv2.imshow('YOLO', np.array(results.render()))
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()