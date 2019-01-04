# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 15:00:04 2019

@author: Administrator

compress image difference
"""

import skimage
import cv2
import imutils

imgA = cv2.imread('bra.jpg')
imgB = cv2.imread('bra.jpg')

grayA = cv2.cvtColor(imgA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imgB, cv2.COLOR_BGR2GRAY)

(score, diff) = skimage.measure.compare_ssim(grayA, grayB, full=True)
diff = (diff*255).astype("uint8")
print("ssim:{}".format(score))

thresh = cv2.threshold(diff, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
# loop over the contours
for c in cnts:
	# compute the bounding box of the contour and then draw the
	# bounding box on both input images to represent where the two
	# images differ
	(x, y, w, h) = cv2.boundingRect(c)
	cv2.rectangle(imgA, (x, y), (x + w, y + h), (0, 0, 255), 2)
	cv2.rectangle(imgB, (x, y), (x + w, y + h), (0, 0, 255), 2)

# show the output images
cv2.imshow("Original", imgA)
cv2.imshow("Modified", imgB)
cv2.imshow("Diff", diff)
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)