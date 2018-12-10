# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 19:50:57 2018

@author: Administrator
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

#def demo():
#    img = cv2.imread('bra.jpg')
#    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#    # Now we split the image to 5000 cells, each 20x20 size
#    cells = [np.hsplit(row,100) for row in np.vsplit(gray,50)]
#    # Make it into a Numpy array. It size will be (50,100,20,20)
#    x = np.array(cells)
#    # Now we prepare train_data and test_data.
#    train = x[:,:50].reshape(-1,400).astype(np.float32) # Size = (2500,400)
#    test = x[:,50:100].reshape(-1,400).astype(np.float32) # Size = (2500,400)
#    # Create labels for train and test data
#    k = np.arange(10)
#    train_labels = np.repeat(k,250)[:,np.newaxis]
#    test_labels = train_labels.copy()
#    # Initiate kNN, train the data, then test it with test data for k=1
#    knn = cv2.ml.KNearest_create()
#    knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)
#    ret,result,neighbours,dist = knn.findNearest(test,k=5)
#    # Now we check the accuracy of classification
#    # For that, compare the result with test_labels and check which are wrong
#    matches = result==test_labels
#    correct = np.count_nonzero(matches)
#    accuracy = correct*100.0/result.size
#    print( accuracy )

def main():
    png = cv2.imread('bra.jpg')
    gray = cv2.cvtColor(png, cv2.COLOR_BGR2GRAY)
    print(type(gray))
    #print("dim:", gray.ndim)
    print("shape:", gray.shape)
    #help(gray.shape)
    # tuple get value
    #print(gray.shape[1])
    # split 5000 cells
    #print(np.vsplit(gray, 960))
    # v:height=1920 , h: width=1080
    cells = ([np.hsplit(row,540) for row in np.vsplit(gray, 960)])
#    #make it into numpy.array
    x = np.array(cells)
#    print(type(x))
#    print(len(x))#960
#    #prepare train_data and test_data
    train = x[:,:50].reshape(-1, 400).astype(np.float32)
    test = x[:,50::100].reshape(-1,400).astype(np.float32)
    #lables for train and test data
    k = np.arange(10)
    train_labels = np.repeat(k,250)[:,np.newaxis]
    print(type(train_labels))
    test_labels = train_labels.copy()
    print(type(test_labels))
    # init knn train data
    knn = cv2.ml.KNearest_create()
    print(type(knn))
#    knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)
#    ret, result,neighbours,dist = knn.findNearest(test,k=5)
#    #
#    matches = result==test_labels 
#    correct = np.count_nonzero(matches)
#    accuracy = correct*100.0/result.size
#    print(accuracy)
#    cv2.imshow('hello',gray)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()
    

if (__name__ == "__main__"):
    main()