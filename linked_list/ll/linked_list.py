# -*- coding: utf-8 -*-
"""
"""
from .node import Node

class LinkedList():
    def __init__(self, array=None):
        self.head = None
        if array != None:
            # maybe need a try for non itterable
            for n in reversed(array):
                self.head = Node(n, self.head)
    
    def __str__(self):
        s = str(self.head)
        head = self.head.next_node
        while head != None:
            s += (", " + str(head))
            head = head.next_node
        return s
    
if __name__ == "__main__":
    # just a basic test for trial
    l = LinkedList([1,2,3])
    print(l)
