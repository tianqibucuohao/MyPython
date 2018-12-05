import os
import os.path as op

def main():
    print("hello")
    root = r"E:\sofe备份"
    ll = os.path.listdir(root)
    for i in range(0,len(ll)):
        print(ll[i])

def findfile(path):
    pass

if (__name__ == "__main__"):
    main()

