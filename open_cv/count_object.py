# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 16:29:43 2019

@author: Administrator
边际检测 Canny
阀值化 threshold
边缘 findContours
"""

import cv2 as cv

def main():
    img = cv.imread('sp.jpg')
    print(type(img))
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    edge = cv.Canny(gray,100,150)
    mo='edge'
    cv.namedWindow(mo, cv.WINDOW_NORMAL)
    cv.resizeWindow(mo, 200,200)
    ts = cv.threshold(gray, 225, 255, cv.THRESH_BINARY_INV)[1]
    findc = ts.copy()
    contours0 = cv.findContours(findc, 
                        cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    #contours = [cv.approxPolyDP(cnt, 3, True) for cnt in contours0]
    print(contours0)
    print(len(contours0))
    
    cv.imshow('threshold',ts)
    cv.imshow(mo,edge)

if (__name__ == "__main__"):
    main()
