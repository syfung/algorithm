# -*- coding: utf-8 -*-
import unittest
from ll.linked_list import LinkedList

class TestLinkedListInit(unittest.TestCase):

    def test_from_int_array(self):
        a = [1,2,3,4]
        self.assertEqual(str(LinkedList(a)), "1, 2, 3, 4")

    def test_from_char_array(self):
        a = ['a','b','c','d']
        self.assertEqual(str(LinkedList(a)), "a, b, c, d")
        
if __name__ == '__main__':
    unittest.main()
