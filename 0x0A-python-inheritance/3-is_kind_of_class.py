#!/usr/bin/python3
"""
defines function to check if an object is from a class
"""


def is_kind_of_class(obj, a_class):
    """function to check an object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class

    Args:
        obj (any): object to check
        a_class(any): class to be checked against
    """

    if isinstance(obj, a_class):
        return True

    return False
