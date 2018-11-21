import numpy as np
import cv2

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
img = cv2.imread('1.jpg', 0)
cv2.imshow('image', img)
k = cv2.waitKey(0)

if  k == 27:
    cv2.destoryAllWindows()
elif k == ord('s'):
    #write an image
    cv2.imwrite('2.png', img)
    cv2.destoryAllWindows()




