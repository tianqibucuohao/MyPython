import numpy as np
import cv2
from matplotlib import pyplot as plt 

img = cv2.imread('1.jpg', 0)
plt.imshow(img, cmpa='gray', interpolation='bicubic')
plt.xticks([]),plt.yticks([])

plt.show()