# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 09:59:39 2019

@author: Administrator

边际检测
"""

import cv2 as cv
#import convenience.grab_contours
from . import imutils
from skimage.filters import threshold_local
import numpy as np

path = "20190218170703.png"
img = cv.imread(path)
ratio = img.shape[0]/500.0
orig = img.copy()

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = cv.GaussianBlur(gray, (5,5), 0)
edged = cv.Canny(gray, 75, 200)

cnts = cv.findContours(edged.copy(),cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key=cv.contourArea,reverse=True)[:5]
for c in cnts:
    per = cv.arcLength(c,True)
    app = cv.approxPolyDP(c,0.02*per,True)
    if (len(app) ==4):
        scr=app
        break

cv.drawContours(img, [scr],-1, (0,255,0),2)    

warped = imutils.four_point_transform(orig,scr.reshape(4,2)*ratio)
warped = cv.cvtColor(warped, cv.COLOR_BGR2GRAY)
t = threshold_local(warped, 11, offset=10, method='gaussian')
warped = (warped>t).astype("uint8")*255
cv.imshow("scan", imutils.resize(warped, height=800))
cv.imshow("canny", img)
cv.waitKey(0)
#cv.destoryWindow()

