import threading
import time

"""
生产者与消费者
"""
 
condition = threading.Condition()
products = 0
 
class Producer(threading.Thread):
#    '''生产者'''
    ix = [0] # 生产者实例个数
             # 闭包，必须是数组，不能直接 ix = 0
    def __init__(self, ix=0):
        super().__init__()
        self.ix[0] += 1
        self.setName('Producer ' + str(self.ix[0]))
 
    def run(self):
        global condition, products
        
        while True:
            if condition.acquire():
                if products < 10:
                    products += 1;
                    print("{}：Rest(10-). Product 1, now all sums= {}".format(self.getName(), products))
                    condition.notify()
                else:
                    print("{}：Rest(10+).Take a break, now all sums= {}".format(self.getName(), products))
                    condition.wait();
                condition.release()
                time.sleep(2)


class Consumer(threading.Thread):
#    '''消费者'''
    ix = [0] # 消费者实例个数
             # 闭包，必须是数组，不能直接 ix = 0
    def __init__(self):
        super().__init__()
        self.ix[0] += 1
        self.setName('Consumer ' + str(self.ix[0]))
 
    def run(self):
        global condition, products
        
        while True:
            if condition.acquire():
                if products > 1:
                    products -= 1
                    print("{}:I product one production.Now all sums= {}".format(self.getName(), products))
                    condition.notify()
                else:
                    print("{}:One product rest.Stop producting.Now all sums= {}".format(self.getName(), products))
                    condition.wait();
                condition.release()
                time.sleep(2)



if __name__ == "__main__":
    for i in range(2):
        p = Producer()
        p.start()
 
    for i in range(5):
        c = Consumer()
        c.start()