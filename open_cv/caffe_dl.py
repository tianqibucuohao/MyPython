# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 10:01:38 2019

@author: Administrator
在opencv dnn 深度神经网络模块与caffe模块使用时
需要下面文件
.prototxt 定义模块结构，如层本身
.caffemodel 包含实际层的权重


待续-没有caffe模型文件
"""
import cv2
import numpy as np

print('loading model...')
p = '../samples/dnn/face_detector/'
m = ''
f = ''
net = cv2.dnn.readNetFromCaffe(p, m)

img = cv2.imread(f)
(h,w) = img.shape[:2]
blob =cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)), 1.0,
	(300, 300), (104.0, 177.0, 123.0))

print('computing object detech..')
net.setInput(blob)
detect = net.forward()