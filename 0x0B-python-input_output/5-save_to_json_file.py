#!/usr/bin/python3
"""defines a function that writes an object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """Saves an object to a text file
        Arguments:
            my_obj (object): object to be saved
            filename (str): file to save to
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
