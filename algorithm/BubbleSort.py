# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 16:45:21 2019

@author: Administrator
Bubble sort

冒泡排序算法实现
    Bubble_Sort_simpleX，几种不同交换值的方式
选择排序算法
    selectSort
插入排序算法    
    InsertionSort
"""

class BS:
    def __init__(self, ls):
        self.r = ls
    
    def swap(self, i, j):
        """ 使用临时变量"""
        tmp = self.r[i]
        self.r[i] = self.r[j]
        self.r[j] = tmp
        
    def swap2(self, i, j):
        """位运算交换"""
        self.r[i] = self.r[i]^self.r[j]
        self.r[j] = self.r[i]^self.r[j]
        self.r[i] = self.r[i]^self.r[j]
        
    def Bubble_Sort_simple(self):
        ls = self.r
        length = len(self.r)
        for i in range(length):
            for j in range(i+1, length):
                if (ls[i]>ls[j]):
                    self.swap(i, j)
                    
    def Bubble_Sort_simple2(self):
        ls = self.r
        length = len(self.r)
        for i in range(length):
            for j in range(i+1, length):
                if (ls[i]>ls[j]):
                    self.swap2(i, j)

    def Bubble_Sort_simple3(self):
        """直接交换数值"""
        ls = self.r
        length = len(self.r)
        for i in range(length):
            for j in range(i+1, length):
                if (ls[i]>ls[j]):
                    self.r[i],self.r[j] = ls[j],ls[i]

    def __str__(self):
        ret = ""
        for i in self.r:
            ret += " %s" % i
        return ret  

class SelectSort:
    def __init__(self, ls):
        self.r = ls
    def selectSort(self):
        ls = self.r
        length = len(self.r)
        for i in range(length):
            minidx = i
            for j in range(i+1, length):
                if (ls[j]<ls[minidx]):
                    minidx = j
            self.r[i],self.r[minidx] = ls[minidx],ls[i]
            
    def __str__(self):
        ret = ""
        for i in self.r:
            ret += " %s" % i
        return ret 

class InsertionSort:
    def __init__(self,ls):
        self.r = ls
    def insertSort(self):
        length = len(self.r)
        ls = self.r
        """向前比较，长度-1"""
        for i in range(length-1):
            curNum, preIdx = ls[i+1],i
            while (preIdx >= 0 and curNum < ls[preIdx]):
                self.r[preIdx+1] = ls[preIdx]
                preIdx -= 1
            self.r[preIdx+1] = curNum
                
    
    def __str__(self):
        ret = ""
        for i in self.r:
            ret += " %s" % i
        return ret 
                    
if (__name__ == '__main__'):
    ls =[1, 4, 8, 2, 9, 0,2,3,10,89,2,4]
    if (0):
        s1 = BS(ls)
        s2 = BS(ls)
        s3 = BS(ls)
        s1.Bubble_Sort_simple()
        s2.Bubble_Sort_simple2()
        s3.Bubble_Sort_simple3()
        print(s1)
        print(s2)
        print(s3)
    if (0):
        s1 = SelectSort(ls)
        s1.selectSort()
        print(s1)
    if (1):
        s1 = InsertionSort(ls)
        s1.insertSort()
        print(s1)
    