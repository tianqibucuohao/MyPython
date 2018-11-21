import threading
import queue
import time
import hashlib

# 锁 演示
class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print( "Starting " + self.name)
       # 获得锁，成功获得锁定后返回True
       # 可选的timeout参数不填时将一直阻塞直到获得锁定
       # 否则超时后将返回False
       # 同步锁
        threadLock.acquire()
        print_time(self.name, self.counter, 2)
        # 释放锁
        threadLock.release()
 
def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1
 
#同步锁
threadLock = threading.Lock()
threadCdsn = threading.Condition()

threads = []

 
# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)
thread3 = myThread(4, "Thread-3", 1)

print(thread1.getName())
 
# 开启新线程
thread1.start()
thread2.start()
thread3.start()
 
# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)
threads.append(thread3)
 
# 等待所有线程完成
for t in threads:
    t.join()
print("Exiting Main Thread")