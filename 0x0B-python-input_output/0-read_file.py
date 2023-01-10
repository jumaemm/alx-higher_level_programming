#!/usr/bin/python3
"""This modue defines a function to read a text file and print it to stdout"""


def read_file(filename=""):
    """reads contents of a file and prints it to stdout"""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
