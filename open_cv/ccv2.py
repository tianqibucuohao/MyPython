import numpy as np
import cv2
from matplotlib import pyplot as plt 

def pltshow(path):
    """show image file by using matplotlib"""
    img = cv2.imread(path, 0)
    plt.imshow(img, cmpa='gray', interpolation='bicubic')
    plt.xticks([]),plt.yticks([])
    plt.show()
    
if (__name__ == "__main__"):
    help(pltshow)
    pltshow('bra.jpg')