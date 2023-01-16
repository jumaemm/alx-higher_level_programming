#!/usr/bin/python3
"""Base model for core functionality"""


class Base:
    """Represents the base model for all shapes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize instance of the Base class"""
        if (id):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
