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
希尔排序算法
    shellsort
合并排序
    megresort
快速排序
    quicksort
    
"""

class BS:
    """冒泡排序"""
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
    """选择排序"""
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
    """插入排序"""
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

class ShellSort:
    """希尔排序"""
    def __init__(self, ls):
        self.r = ls
    def shellSort(self):
        lens = len(self.r)
        gap = 0
        while (gap < lens):
            gap = gap*3 + 1
        
        while (gap >0):
            for i in range(gap, lens):
                curNum, preidx = self.r[i], i-gap
                while (preidx >= 0 and curNum < self.r[preidx]):
                    self.r[preidx + gap] = self.r[preidx]
                    preidx -= gap
                self.r[preidx+gap] = curNum
                #print(self.r)
            gap //= 3
            
    def __str__(self):
        ret = ""
        for i in self.r:
            ret += " %s" % i
        return ret     

class MergeSort:
    """合并排序"""
    def __init__(self, ls):
        self.r = ls
    def mergeSort(self, ls):
      pass
        
    def __str__(self):
        ret = ""
        for i in self.r:
            ret += " %s" % i
        return ret
    
class QuickSort:
    """快速排序"""
    def __init__(self, ls):
        self.r = ls
    def quickSort(self):
        nums = self.r
        def quick(nums):
            if (len(nums) <= 0):
                return nums
            pv = nums[0]
            lf = []
            rt = []
            for i in range(1, len(nums)):
                if (nums[i]<pv):
                    nums[i] = pv
                    lf.append(nums[i])
            for i in range(1, len(nums)):
                if (nums[i]>=pv):
                    nums[i] = pv
                    rt.append(nums[i])
            return quick(lf)+[pv]+quick(rt)
    
    def __str__(self):
        ret = ""
        for i in self.r:
            ret += " %s" % i
        return ret    
    
if (__name__ == '__main__'):
    ls =[1, 4, 8, 2, 9, 0,12,23,10,89,32,46,30,27]
    if (0):#冒泡排序
        s1 = BS(ls)
        s2 = BS(ls)
        s3 = BS(ls)
        s1.Bubble_Sort_simple()
        s2.Bubble_Sort_simple2()
        s3.Bubble_Sort_simple3()
        print(s1)
        print(s2)
        print(s3)
    if (0):#选择排序
        s1 = SelectSort(ls)
        s1.selectSort()
        print(s1)
    if (0):#插入排序
        s1 = InsertionSort(ls)
        s1.insertSort()
        print(s1)
    if (0):
        s1 = ShellSort(ls)
        s1.shellSort()
        print(s1)
    if (1):
        s1 = QuickSort(ls)
        s1.quickSort()
        print(s1)