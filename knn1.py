#Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.
import cv2
import numpy as py
import matplotlib.pyplot as plt

traindata = py.random.randint(0,100,(25,2)).astype(py.float32)
responses = py.random.randint(0,2,(25,1)).astype(py.float32)

red = traindata[responses.ravel()==0]
plt.scatter(red[:,0],red[:,1],80,'r','^')

blut = traindata[responses.ravel() ==1]
plt.scatter(blut[:,0],blut[:,1],80,'b','^')

nc = py.random.randint(0,100,(1,2)).astype(py.float32)
plt.scatter(nc[:,0], nc[:,1], 80,'g','o')

knn = cv2.ml.KNearest_create()
#knn = cv2.ml_KNearest()
#cv2.ml_StatModel().KNearest_create()
#knn.train(traindata,responses)
knn.train(traindata,cv2.ml.ROW_SAMPLE,responses)
ret,result,nb,dist = knn.findNearest(nc,3)

print("ret :", ret)
print("result :", result)
print("nb :", nb)
print("dist :", dist)
plt.show()
 
