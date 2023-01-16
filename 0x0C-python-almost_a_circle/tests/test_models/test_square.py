#!/usr/bin/python3
"""Unittests for the models.square.py"""
import unittest
from models.base import Base
from models.square import Square


class TestSquare_init(unittest.TestCase):
    """Test instantiation of Square model"""

    def test_square_inheritance(self):
        self.assertIsInstance(Square(5), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        s1 = Square(5)
        s2 = Square(6)
        self.assertEqual(s1.id, s2.id - 1)

    def test_two_args(self):
        s1 = Square(10, 2)
        s2 = Square(2, 10)
        self.assertEqual(s1.id, s2.id - 1)

class TestSquare_area(unittest.TestCase):
    """Test area method"""

    def test_area_normal(self):
        self.assertEqual(36, Square(6, 0, 0, 1).area())

    def test_area_large(self):
        s = Square(999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999999998000000000000000001, s.area())

    def test_area_modified(self):
        s = Square(4, 0, 0, 1)
        s.size = 8
        self.assertEqual(64, s.area())

    def test_area_one_arg(self):
        s = Square(2, 10, 1, 1)
        with self.assertRaises(TypeError):
            s.area(1)
