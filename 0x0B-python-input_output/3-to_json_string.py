#!/usr/bin/python3
"""Defines a function to return json representation of an object"""
import json


def to_json_string(my_obj):
    """Return json representation of a string
        Arguments:
            my_obj (str): string object to be serialized
        Return: json rep of the object
    """
    return (json.dumps(my_obj))
