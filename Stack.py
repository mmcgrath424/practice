import os
from LinkedList import LinkedList

class Stack():
    def __init__(self):
        self.stacked = LinkedList()
    
    def push(self,value):
        self.stacked.prepend(value)

    def pop(self):
        if self.stacked.get_length() > 0:          
            value = self.stacked.get_node(0).get_value()
            self.stacked.remove(0)
            return value
        else:
            return None
    
    def print_stack(self):
        self.stacked.print_list()


if __name__=='__main__':
    test_stack = Stack()
    for x in range (1,20):
        test_stack.push(x)

    test_stack.print_stack()
    while True:
        value = test_stack.pop()
        if value != None:
            print (value)
        else:
            break
