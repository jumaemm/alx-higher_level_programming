#!/usr/bin/python3
"""function that adds a new attribute to an object if it’s possible"""


def add_attribute(obj, name, value):
    """Adds a new attrib to obj

    Args:
        obj (type): object to be modified
        name (str): Attribute name
        value (any): Attribute value
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
