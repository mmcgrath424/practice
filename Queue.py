import os
from LinkedList import LinkedList
class Queue():
    def __init__(self):
        self.queued = LinkedList() 

    def enqueue(self,value):
        self.queued.append(value)

    def dequeue(self):
        if self.queued.get_length() > 0:          
            value = self.queued.get_node(0).get_value()
            self.queued.remove(0)
            return value
        else:
            return None

    def print_queue(self):
        self.queued.print_list()


if __name__=='__main__':
    test_queue = Queue()
    for x in range (1,20):
        test_queue.enqueue(x)

    test_queue.print_queue()
    while True:
        value = test_queue.dequeue()
        if value != None:
            print (value)
        else:
            break
