#!/usr/bin/python3
"""defines a function to append a string to the end of a file"""


def append_write(filename="", text=""):
    """Append string to the end of a file
        Arguments:
            filename (str): name of file
            text (str): string to be appended
        Return: number of chars appended
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
