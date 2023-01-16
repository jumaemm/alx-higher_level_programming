#!/usr/bin/python3
"""Represents a class rectangel inheriting from the Base class"""
from models.base import Base


class Rectangle(Base):
    """Represents a Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle instance
        Arguments:
            width (int): width of the rectangle
            height (int): height of the recatngle
            x (int): x coordinate of the rectangle
            y (int): y coordinate of the rectangle
            id (int): id of the rectangle
        """

        self.id = super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """Override string method to rep the rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    @property
    def width(self):
        """get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if (type(value) != int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height of the rectangle"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """set the value of the x coordinate"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Print the rectangle to stdout """
        if self.width == 0 or self.height == 0:
            print("")
            return
        for j in range(self.y):
            print("")
        for i in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Update the rectangle instance with args
        Arguments:
            *args:
                arg1 (int): 1st argument which is id
                arg2 (int): 2nd arg which is width
                arg3 (int): 3rd arg which is height
                arg4 (int): 4th arg which is x
                arg5 (int): 5th arg which is y
        """
        if (args) and (len(args) != 0):
            count = 0
            for arg in args:
                if count == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif count == 1:
                    self.width = arg
                elif count == 2:
                    self.height = arg
                elif count == 3:
                    self.x = arg
                elif count == 4:
                    self.y = arg
                count += 1
        elif (kwargs) and (len(kwargs) != 0):
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Return the dictionary representation of the instance."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
