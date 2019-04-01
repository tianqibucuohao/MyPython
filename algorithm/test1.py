# -*- coding: utf-8 -*-

"""
斐波那契数列（Fibonacci sequence）
"""

def fs(n):
    if (n < 2):
        return 1
    else:
        fsum = fs(n-1)+fs(n-2)
        return fsum

def fbGen(n):
    """
    有问题只打印下标
    """
    a, b = 0, 1
    while n>0:
        yield a
        a, b, n = b, a+b, n-1

def main():
    """
    2种赋值写法
    """
    if (0):
        ls = []
        for i in range(6):
            ls.append(fs(i))
    else:
        ls = [i for i in range(6)]
    print(ls)
#    l=[a for a in fbGen(6)]
#    print(l)

if (__name__ == "__main__"):
    main()