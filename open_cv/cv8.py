import cv2
import numpy as np

img = cv2.imread('blox.jpg')

px = img[100,100]
print(px)

blue = img[100, 100,0]
print(blue)

img[100, 100] = [255,255,255]
print( img[100,100])

img.item(10,10,2)

img.itemset((10,10,2),100)
img.item(10,10,2)

print( img.shape)

print( img.size)

print( img.dtype)

ball = img[80:150, 130,100]
# roi  copy or clip area
img[100:300,100:400] = ball

b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))
#to gray
b = img[:,:,0]
# make borders for image(padding)

from matplotlib import pyplot as plt
BLUE = [255,0,0]
img1 = cv2.imread('2.jpg')

replicate = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)

plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

plt.show()