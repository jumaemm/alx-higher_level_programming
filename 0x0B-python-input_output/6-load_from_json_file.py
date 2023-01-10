#!/usr/bin/python3
"""Defines a function that creates an object from a json file"""
import json


def load_from_json_file(filename):
    """Create an object from a JSON file
        Arguments:
            filename (str): name of the file to be created
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return json.load(f)
