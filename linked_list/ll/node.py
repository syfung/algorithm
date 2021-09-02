# -*- coding: utf-8 -*-
"""
"""

class Node():
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def set_next_node(self, next_node):
        self.next_node = next_node
        
    def __str__(self):
        return str(self.data)
