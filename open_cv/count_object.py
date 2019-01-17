# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 16:29:43 2019

@author: Administrator
边际检测
"""

import cv2 as cv

def main():
    img = cv.imread('bra.jpg')
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    edge = cv.Canny(gray,100,150)
    mo='edge'
    cv.namedWindow(mo, cv.WINDOW_NORMAL)
    cv.resizeWindow(mo, 200,200)
    cv.imshow(mo,edge)
    

if (__name__ == "__main__"):
    main()
