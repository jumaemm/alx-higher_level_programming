#!/usr/bin/python3
"""Represents a square subclass of rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square"""

    def __init__(self, size):
        """Initialize the square

        Args:
            size (int): side length of the square
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
