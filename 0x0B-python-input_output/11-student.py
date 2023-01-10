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

    def to_json(self, attrs=None):
        """Retrieves a dict representation of a Student instance"""
        if (type(attrs) == list and
                all(type(item) == str for item in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance

        Arguments:
            json (dict): the values to replace with
        """
        for key, value in json.items():
            setattr(self, key, value)
