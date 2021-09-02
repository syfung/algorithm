# -*- coding: utf-8 -*-
"""
"""
from .node import Node

class LinkedList():
    def __init__(self, array=None):
        # Always have a empty node at the start to make live easier
        self.head = Node(None)
        if array != None:
            for n in array:
                self.head = Node(n, self.head)
    
    def __str__(self):
        s = ""
        head = self.head
        while head != None:
            s += (", " + str(head))
            head = head.next_node
        return s
    
if __name__ == "__main__":
    l = LinkedList([1,2,3])
    print(l)
