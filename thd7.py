import threading
import time

class MyThd(threading.Thread):
    def __init__(self, threadid, name, counter):
        threading.Thread.__init__(self)
        self.threadid=threadid
        self.name=name
        self.counter=counter
    
    def run(self):
        print("name =%s, id=%d, cnt=%d" % (self.name, self.threadid, self.counter))
        #print("t.id=%d" % threading.Thread.current_thread())
        threadLock.acquire()
        #线程内调用的函数需要是全局，使用同步不能调用类内函数
        do(self.name, self.threadid, self.counter)
        threadLock.release()

def do(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

def main():
    threads = []
    thread1 = MyThd(1, "Thread-1", 4)
    thread2 = MyThd(2, "Thread-2", 2)
    thread3 = MyThd(4, "Thread-3", 4)
    # 开启新线程
    thread1.start()
    thread2.start()
    thread3.start()
    
    # 添加线程到线程列表
    threads.append(thread1)
    threads.append(thread2)
    threads.append(thread3)
    for t in threads:
       
        t.join()
    print("over")


if (__name__ == "__main__"):
    #同步变量放到函数里面，提示出错
    threadLock = threading.Lock()
    main()