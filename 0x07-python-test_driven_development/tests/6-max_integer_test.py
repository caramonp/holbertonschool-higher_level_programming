#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxIntegrer(unittest.TestCase):
    
    def test_max_integer(self):
        list = [1, 2, 4, 3]
        max_integer([list])
        self.assertEqual(list.max_integrer, 4)


if __name__ == '__main__':
    unittest.main()
