#!/usr/bin/python3
"""function to srite to a text file"""


def write_file(filename="", text=""):
    """write text data to a file with given filename
        Arguments:
            filename (str): name of file to open
            text (str): text string to write to file
        Return : number of chars written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
