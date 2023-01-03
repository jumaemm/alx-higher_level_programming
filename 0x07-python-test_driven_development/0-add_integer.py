#!/usr/bin/python3
"""This is a module to add two integers"""


def add_integer(a, b=98):
    """Return addition of ints a and b

    If float, a and b must be casted to integers

    Raises:
        TypeError: a or b is a non-integer or non-float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
