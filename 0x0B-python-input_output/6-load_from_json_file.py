#!/usr/bin/python3
"""
A function that creates an Object from a "JSON file".
"""


import json


def load_from_json_file(filename):
    """ Load an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read and deserialize.

    Returns:
        object: The Python object loaded from the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
