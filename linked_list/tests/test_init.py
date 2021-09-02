# -*- coding: utf-8 -*-
import unittest
from ll.linked_list import LinkedList

class TestLinkedListInit(unittest.TestCase):

    def test_from_int_array(self):
        a = [1,2,3,4]
        self.assertEqual(str(LinkedList(a)), "1, 2, 3, 4")

if __name__ == '__main__':
    unittest.main()
