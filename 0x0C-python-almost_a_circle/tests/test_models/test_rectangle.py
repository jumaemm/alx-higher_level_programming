#!/usr/bin/python3
"""Unittests for models.rectangle.py"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle_init(unittest.TestCase):
    """test insantiation of rectangle"""

    def test_rectangle_inheritance(self):
        """test if rectangle inherits form Base"""
        self.assertIsInstance(Rectangle(2, 6), Base)

    def test_rectangle_two_recs(self):
        r1 = Rectangle(2, 4)
        r2 = Rectangle(7, 9)
        self.assertEqual(r1.id, r2.id - 1)
