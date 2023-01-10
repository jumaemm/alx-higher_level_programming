#!/usr/bin/python3
"""Return string rep of a json object"""
import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string
        Arguments:
            my_str: JSON string reprexentation
        Return: Python object
    """
    return json.loads(my_str)
