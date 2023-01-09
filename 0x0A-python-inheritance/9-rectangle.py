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

    def __str__(self):
        """string rep of a rectangle"""

        rect = "[" + str(self.__class__.__name__) + "] "
        rect += str(self.__width) + "/" + str(self.__height)
        return rect

    def area(self):
        """Returns the area of the rectangle"""

        return (self.__width * self.__height)
