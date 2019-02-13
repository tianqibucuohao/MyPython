# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 15:56:13 2019

@author: Administrator

tuple[:n] >> [0:n)
切片区间：0 <= x < n

"""

import cv2 

img = cv2.imread('bra.jpg')
print(type(img))
(w,h) = img.shape[:2]
#help(img.shape)

print(type(img.shape))
print(w,h)