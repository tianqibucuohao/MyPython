import cv2
import numpy as np

img = cv2.imread('j.png',0)
#腐蚀
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
#膨胀
dilation = cv2.dilate(img,kernel,iterations = 1)
#开放
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
#闭合
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
#形态
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
#顶端
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
#黑端
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

# Rectangular Kernel
>>> cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
array([[1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]], dtype=uint8)

# Elliptical Kernel
>>> cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
array([[0, 0, 1, 0, 0],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [0, 0, 1, 0, 0]], dtype=uint8)

# Cross-shaped Kernel
>>> cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
array([[0, 0, 1, 0, 0],
       [0, 0, 1, 0, 0],
       [1, 1, 1, 1, 1],
       [0, 0, 1, 0, 0],
       [0, 0, 1, 0, 0]], dtype=uint8)