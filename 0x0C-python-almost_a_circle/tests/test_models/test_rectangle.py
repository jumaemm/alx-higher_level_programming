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

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(3, 7, 0, 0, 1).__width)

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(3, 7, 0, 0, 1).__height)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(3, 7, 0, 0, 1).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(3, 7, 0, 0, 1).__y)

    def test_width_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.width)

    def test_width_setter(self):
        r = Rectangle(3, 7, 0, 0, 1)
        r.width = 9
        self.assertEqual(9, r.width)

    def test_height_getter(self):
        r = Rectangle(3, 7, 0, 0, 1)
        self.assertEqual(7, r.height)

    def test_height_setter(self):
        r = Rectangle(3, 7, 0, 0, 1)
        r.height = 10
        self.assertEqual(10, r.height)

class TestRectangle_area(unittest.TestCase):
    """test area method"""

    def test_area_normal(self):
        r = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(20, r.area())

    def test_area_large(self):
        r = Rectangle(999999999999999, 999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999998999000000000000001, r.area())

    def test_area_modified(self):
        r = Rectangle(1, 3, 1, 1, 1)
        r.width = 7
        r.height = 14
        self.assertEqual(98, r.area())

    def test_area_arg(self):
        r = Rectangle(2, 10, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.area(1)
