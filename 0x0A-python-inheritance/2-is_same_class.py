#!/usr/bin/python3
"""
check for inhertance
"""


def is_same_class(obj, a_class):
    """Check if obj is an instance of a_class

    Arguments:
        obj (any): object to check
        a_class (type): class to be checked against
    """

    if (type(obj) == a_class):
        return (True)
    return (False)
