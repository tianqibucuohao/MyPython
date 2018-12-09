# -*- coding: utf-8 -*-
import numpy as np

def createarray():
    """create array use numpy function"""
    print(np.zeros(10,dtype=int))
    print(np.ones((3,2), dtype=float))
    print(np.full((3,5),10,dtype=float))
    #np.random.seek(0)
    x2 = np.random.randint(10,size=(3,4))
    print(x2.shape)#3*4
    print(x2.ndim)# 2 dim
    print(x2.dtype)# int32
    print(x2.itemsize)
    print(x2.nbytes)

def main():
    print(np.__version__)
    createarray()
    ret = 0
    # range(n)  eq i < n
    # 
#    for i in range(100):
#        ret += i
#        
#    print(ret)
#    lnp = np.array([range(i,i+3) for i in [2,4,6]])
#    print(type(lnp))
#    ll = []
#    for i in [2,4,6]:
#        ll.append(np.array(range(i,i+3)))
#    print(type(ll))
#    print(type(ll[0]))
    

if (__name__ == "__main__"):
    main()
