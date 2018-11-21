import threading
import time
# 条件变量 演示
class Consumer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def consume(self):
        global condition
        global items

        condition.acquire()
        if len(items) == 0:
            condition.wait()
            print ("Consumer notify: no item to consume")
        items.pop()
        print("Consumer notify: consumed 1 item")
        print("Consumer nofity: items to consume are "\
              + str(len(items)))
        condition.notify()
        condition.release()

    def run(self):
        for i in range(0, 20):
            time.sleep(4)
            self.consume()

class Producer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def produce(self):
        global condition
        global items

        condition.acquire()
        if len(items) == 10:
            condition.wait()
            print ("Producer notify: item producted are"\
                   + str(len(items)))
            print("Producer nofity: stop the production!!")
        items.append(1)
        print("Producer nofity: total items producted "\
              + str(len(items)))
        condition.notify()
        condition.release()

    def run(self):
        for i in range(0, 20):
            time.sleep(1)
            self.produce()



items = []
#抢占式
condition = threading.Condition()
producer = Producer()
consumer = Consumer()
producer.start()
consumer.start()
producer.join()
consumer.join()