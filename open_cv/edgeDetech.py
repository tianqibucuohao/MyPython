# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 09:59:39 2019

@author: Administrator

边际检测
"""

import cv2 as cv
#import convenience.grab_contours
import imutils

path = "20190218170703.png"
img = cv.imread(path)
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

warped = imutils.four_point_transform(org,scr.reshape(4,2)*ratio)

cv.imshow("canny", img)
cv.waitKey(0)
#cv.destoryWindow()

