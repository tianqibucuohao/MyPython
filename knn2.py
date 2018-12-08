# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 19:50:57 2018

@author: Administrator
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    png = cv2.imread('bra.jpg')
    gray = cv2.cvtColor(png, cv2.COLOR_BGR2GRAY)
    # split 5000cells
    print(type(gray))  
#    cells = [np.hsplit(row,100) for row in np.vsplit(gray, 50)]
#    #make it into numpy.array
#    x = np.array(cells)
#    #prepare train_data and test_data
#    train = x[:,:50].reshape(-1, 400).astype(np.float32)
#    test = x[:,50::100].reshape(-1,400).astpye(np.float32)
#    #lables for train and test data
#    k = np.arange(10)
#    train_labels = np.repeat(k,250)[:,np.newaxis]
#    test_labels = train_labels.copy()
#    # init knn train data
#    knn = cv2.ml.KNearest_create()
#    knn.train(train, cv2.ml.ROW_SAMPLE, train_labels)
#    ret, result,neighbours,dist = knn.findNearest(test,k=5)
#    #
#    matches = result==test_labels 
#    correct = np.count_nonzero(matches)
#    accuracy = correct*100.0/result.size
#    print(accuracy)
    

if (__name__ == "__main__"):
    #main()
    help(len)