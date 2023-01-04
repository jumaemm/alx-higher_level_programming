#!/usr/bin/python3
"""This module prints a square"""


def print_square(size):
    """Print a square of #'s

    Arguments:
        size (int): the length of a side of the square.
    Raises:
        TypeError: if size isn't an integer
        ValueError: If size < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="")for j in range(size)]
        print("")
