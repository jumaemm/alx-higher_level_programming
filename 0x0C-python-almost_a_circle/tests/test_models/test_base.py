#!/usr/bin/python3
"""Unittests for the base model functions"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_Init(unittest.TestCase):
    """Test instantiation of the base class"""
    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_float_id(self):
        self.assertEqual(5.5, Base(5.5).id)
        
    def test_nb_objects_after_id(self):
        b1 = Base()
        b2 = Base(7)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_dict_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_str_id(self):
        self.assertEqual("Boy", Base("Boy").id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

class TestBase_to_json_string(unittest.TestCase):
    """test to_json_string method"""

    def test_to_json_string_rectangle_type(self):
        r = Rectangle(8, 12, 1, 2, 3)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_to_json_string_rectangle_one_dict(self):
        r = Rectangle(8, 12, 1, 2, 3)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)

    def test_to_json_string_rectangle_two_args(self):
        r1 = Rectangle(8, 12, 1, 2, 3)
        r2 = Rectangle(3, 7, 10, 15, 5)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 107)

    def test_to_json_string_square_type(self):
        s = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string(None))

class TestBase_save_to_file(unittest.TestCase):
    """Test save to file functionality"""

    @classmethod
    def tearDown(self):
        """Delete any created files."""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_one_rec(self):
        r = Rectangle(8, 12, 1, 2, 3)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_one_square(self):
        s = Square(6, 1, 2, 3)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 38)

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())
