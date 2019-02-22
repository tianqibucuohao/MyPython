# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 16:29:43 2019

@author: Administrator
边际检测 Canny
阀值化 threshold
边缘 findContours
侵蚀 erode
膨胀 dilate
位运算 bitwise_and,bitwise_or/xor/not
旋转 getRotationMatrix2D
高斯模糊 GaussianBlur
矩形 rectangle
圆形实心 circle
直线 line
文字 putText
getPerspectiveTransform
warpPerspective
arcLength
approxPolyDP
"""

import cv2 as cv
from . import convenience

def main():
    img = cv.imread('sp.jpg')
    #print(type(img))
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    edge = cv.Canny(gray,30,150)
    mo='edge'
    cv.namedWindow(mo, cv.WINDOW_NORMAL)
    cv.resizeWindow(mo, 200,200)
    ts = cv.threshold(gray, 225, 255, cv.THRESH_BINARY_INV)[1]
    findc = ts.copy()
    contours0 = cv.findContours(findc, 
                        cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    #contours = [cv.approxPolyDP(cnt, 3, True) for cnt in contours0]
#    outp = img.copy()
#    for c in len(contours0):
#        cv.drawContours(outp, [c], -1, (240,0,193),3)
#        cv.imshow("contours",outp)
#        cv.waitkey(0)
    #print(contours0)
    #print(len(contours0))
    
    #cv.imshow('threshold',ts)
    mask = ts.copy()
    #mask = cv.erode(mask, None, iterations=5)
    mask = cv.dilate(mask, None, iterations=5)
    output = cv.bitwise_or(img, img, mask=mask)
    cv.imshow("Output", output)
    cv.imshow(mo,mask)
    cv.waitKey(0)

def test():
    path = "20190218170703.png"
    img = cv.imread(path)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = cv.GaussianBlur(gray, (5,5),0)
    edged = cv.Canny(gray, 75, 200)
    
    
if (__name__ == "__main__"):
    main()
