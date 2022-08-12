#!/usr/bin/env python3
import torch
print(torch.__version__)
# Model
model = torch.hub.load('/home/zj/_github_/folder_python/yolov3', 'yolov3',source='local')  # or yolov3-spp, yolov3-tiny, custom
# model = torch.hub.load('ultralytics/yolov3', 'yolov3')  # or yolov3-spp, yolov3-tiny, custom
# Images
img = '/home/zj/Downloads/zidane.jpg'  # or file, Path, PIL, OpenCV, numpy, list
# img = 'https://ultralytics.com/images/zidane.jpg'  # or file, Path, PIL, OpenCV, numpy, list
# Inference
results = model(img)
# Results
results.print()  # or .show(), .save(), .crop(), .pandas(), etc.