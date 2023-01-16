#!/usr/bin/python3
"""Contains Square class inheriting from Base"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent the square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the Square
        Arguments:
            size (int): length of one side of the square
            x (int): x coordinate of the square
            y (int): y coordinate of the square
            id (int): id of the square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return str rep of the square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    @property
    def size(self):
        """get the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """set the size of the square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the square instance with args
        Arguments:
            *args:
                arg1 (int): 1st argument which is id
                arg2 (int): 2nd arg which is size
                arg3 (int): 3th arg which is x
                arg4 (int): 4th arg which is y
        """
        if (args) and (len(args) != 0):
            count = 0
            for arg in args:
                if count == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif count == 1:
                    self.size = arg
                elif count == 2:
                    self.x = arg
                elif count == 3:
                    self.y = arg
                count += 1
        elif (kwargs) and (len(kwargs) != 0):
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Return the dictionary representaton of the instance."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
