#!/usr/bin/python3
"""Defines a function thet returns a Pascal's triangle"""


def pascal_triangle(n):
    """returns a list of ints repping thePascal's triangle of n

    Arguments:
        n (int): the depth of the triangle
    """
    if n <= 0:
        return []

    pascal = [[1]]
    while len(pascal) != n:
        triangle = pascal[-1]
        sub_triangle = [1]
        for i in range(len(triangle) - 1):
            sub_triangle.append(triangle[i] + triangle[i + 1])
        sub_triangle.append(1)
        pascal.append(sub_triangle)
    return pascal
