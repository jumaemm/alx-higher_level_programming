#!/usr/bin/python3
"""class Rectangle is a subclass of BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle as a subclass of BaseGeometry"""

    def __init__(self, width, height):
        """Initialize the rectangle

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
