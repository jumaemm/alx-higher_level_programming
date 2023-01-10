#!/usr/bin/python3
"""Contains Student class"""


class Student:
    """Repressents a Student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student object
            Arguments:
                first_name (str): first name of the  student
                last_name (str): last name of the student
                age (int): age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dict representation of a Student instance"""
        return self.__dict__
