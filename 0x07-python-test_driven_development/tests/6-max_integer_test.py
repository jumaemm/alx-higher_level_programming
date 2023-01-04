#!/usr/bin/python3
"""Unittests for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Class of test cases for max integer function"""

    def test_normal_list(self):
        """Test a normal ordered list of ints"""
        normal = [2, 5, 7, 8, 9]
        self.assertEqual(max_integer(normal), 9)

    def test_unordered_list(self):
        """Tests an unordered list of ints"""
        unordered_list = [5, 2, 6, 3]
        self.assertEqual(max_integer(unordered_list), 6)

    def test_float_list(self):
        """Tests a list of floats"""
        float_list = [2.3, 4.5, 6.7, 8.9]
        self.assertEqual(max_integer(float_list), 8.9)

    def test_float_mix(self):
        """Tests a list of floats and ints"""
        float_mix = [3.4, 5, 6, 6.8, 2, 4.5]
        self.assertEqual(max_integer(float_mix), 6.8)

    def test_sring(self):
        """Tests a string"""
        string = "Michael"
        self.assertEqual(max_integer(string), "l")

    def test_string_list(self):
        """Tests a list of strings"""
        string_list = ["Tom", "Richard", "Harry"]
        self.assertEqual(max_integer(string_list), "Tom")

    def test_empty_list(self):
        """Tests an empty list"""
        empty_list = []
        self.assertEqual(max_integer(empty_list), None)

    def test_one_element(self):
        """Tests a list of only one element"""
        one_elem = [7]
        self.assertEqual(max_integer(one_elem), 7)

    def test_empty_string(self):
        """Tests for an empty string"""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()
