#!/usr/bin/python3
"""Unittests for max_integer(list=[]) function"""

import unittest


class TestMaxInteger(unittest.TestCase):
    """declared class to test the cases"""

    def setUp(self):
        """method to import from the file to test"""
        max_integer = __import__('6-max_integer').max_integer
        self.max_integer = max_integer

    def test_positive_integers(self):
        """method to test positive numbers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        
    def test_negative_integers(self):
        """method to test negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        
    def test_mixed_integers(self):
        """method to test mixed numbers"""
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)
        
    def test_single_integer(self):
        """method to test single-int numbers"""
        self.assertEqual(max_integer([5]), 5)
        
    def test_empty_list(self):
        """method to test if list is empty"""
        self.assertIsNone(max_integer([]))
