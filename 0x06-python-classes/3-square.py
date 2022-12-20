#!/usr/bin/python3

"""define a square"""


class Square:
    """This is the square"""

    def __init__(self, size=0):
        """Initialize the square

        Args:
            size(int): size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Compute the area of the square"""

        return (self.__size * self.__size)
