#!/usr/bin/python3
"""empty class"""


class BaseGeometry():
    """empty class for now"""

    def area(self):
        """Throws exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates that value is an int

        Args:
            name (str): name of param
            value (int): The param to be validated
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
