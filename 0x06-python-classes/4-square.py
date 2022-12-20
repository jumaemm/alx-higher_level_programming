#!/usr/bin/python3

"""define a square"""


class Square:
    """This is the square"""

    def __init__(self, size=0):
        """Initialize the square
        Args:
            size(int): size of the square
        """

        self.size = size

    def area(self):
        """Compute the area of the square"""

        return (self.__size * self.__size)

    @property
    def size(self):
        """get size"""

        return (self.__size)

    @size.setter
    def size(self, value):
        """Set size value

        Args:
            value(int): value to set
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
