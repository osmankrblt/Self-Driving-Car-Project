import numpy as np
import cv2
import torch

"""
!python export.py --weights "D:/webots self driving car/yolov5/runs/train/yolo_road_det6/weights/best.pt" --include tflite 
"""
repo = "D:/Python Project/yolov5"

#model = torch.hub.load(repo, model="custom", source="local", path='D:/webots self driving car/yolov5/runs/train/yolo_road_det6/weights/best.pt')

class detect:
    def __init__(self):
        repo = "D:/Python Project/yolov5"

        self.model = torch.hub.load(repo, model="custom", source="local",
                                    path='D:/Python Project/Self Driving Car Project/Detection/best.pt')
    def detectAndShow(self,frame):




            # Make detections
        results = self.model(frame)

        return results



