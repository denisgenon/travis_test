# -*- coding: utf-8 -*- 

import unittest
from add import add
 
class TestAddFunction(unittest.TestCase):

    def test_add_function(self):
    	self.assertEqual(add(40, 1), 41)
        self.assertEqual(add(40, 2), 42)
        self.assertEqual(add(40, 3), 43)

if __name__ == '__main__':
    unittest.main()
