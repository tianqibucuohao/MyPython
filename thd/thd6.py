import time
from threading import Thread, Event
import random


#事件 演示 - 不会结束

class Consumer(Thread):
    def __init__(self, items, event):
        Thread.__init__(self)
        self.items = items
        self.event = event

    def run(self):
        while True:
            time.sleep(2)
            self.event.wait()
            item = self.items.pop()
            print("Consumer notify: %d poped from list by %s"
                  %(item, self.name))
            if (len(self.items) == 0):
                break

class Producer(Thread):
    def __init__(self, items, event):
        Thread.__init__(self)
        self.items = items
        self.event = event

    def run(self):
        global item
        for i in range(10):
            time.sleep(2)
            item = random.randint(0, 10)
            self.items.append(item)
            print ("Producer nofity: item N %d appended to list by %s"
                   % (item, self.name))
            print ("Producer notify: event set by %s "
                   % self.name)
            self.event.set()
            print("Produce notify: event clear by %s\n"
                  % self.name)
            self.event.clear()
            

items = []
event = Event()

producer = Producer(items, event)
consumer = Consumer(items, event)
producer.start()
consumer.start()
producer.join()
consumer.join()
print("end of show time")