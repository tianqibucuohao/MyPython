import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    # numpy.random.rand() :[0,1]均匀分布的随机样本
    # numpy.random.randn():标准正态分布N(0,1)
    # numpy.random.randint(low,high,(个数，元组)):区间离散均匀分布的整数
    #t=py.random.randint(0,100,(25,3))
    #print(t)
    print(type(np.random.randint(0,100,(25,2))))
    traindata = np.random.randint(0,100,(25,2)).astype(np.float32)
    responses = np.random.randint(0,2,(25,1)).astype(np.float32)
    
    red = traindata[responses.ravel()==0]
    plt.scatter(red[:,0],red[:,1],80,'r','^')
    #print(red)
    # [:,0] numpy 取所有行的第0个数据
    # [:,1] numpy 取所有行的第1个数据
    #print("red[:,0]",red[:,0])
    #print("red[:,1]",red[:,1])
    
    blut = traindata[responses.ravel() ==1]
    #print(blut)
    plt.scatter(blut[:,0],blut[:,1],90,'b','s')
    
    nc = np.random.randint(0,100,(1,2)).astype(np.float32)
    plt.scatter(nc[:,0], nc[:,1], 80,'g','o')
    
    knn = cv2.ml.KNearest_create()
    #knn = cv2.ml_KNearest()
    #cv2.ml_StatModel().KNearest_create()
    #knn.train(traindata,responses)
    knn.train(traindata,cv2.ml.ROW_SAMPLE,responses)
    # 查看对象或函数说明
    #help(knn)
    #help(knn.train)
    ret,result,nb,dist = knn.findNearest(nc,3)
    
    print("ret :", ret)
    print("result :", result)
    print("nb :", nb)
    print("dist :", dist)
    #rr = knn.isClassifier()
    #print("is classifier:", rr)
    #print("r:", r)
    plt.show()
    #help(knn)
    
if (__name__ == "__main__"):
    main()
 
