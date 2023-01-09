#!/usr/bin/python3
"""Class MyInt inheriiting from int"""


class MyInt(int):
    """Represents an implementation of int with operators inverted"""

    def __eq__(self, value):
        """Switch == with !="""
        return self.real != value

    def __ne__(self, value):
        """Switch != with =="""
        return self.real == value
