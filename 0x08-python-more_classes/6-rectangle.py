#!/usr/bin/python3
"""This module includes the Rectangle class"""


class Rectangle:
    """Represents a rectangle
    Attributes:
        number_of_instances (int): number of rectangle instances.
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Init a new Rectangle object.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    def __str__(self):
        """Return the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        arr = []
        for i in range(self.__height):
            [arr.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                arr.append("\n")
        return ("".join(arr))

    def __repr__(self):
        """Return a string representation of the rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Goodbye Rectangle"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Area of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (self.__width * self.__height)

    def perimeter(self):
        """Perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
