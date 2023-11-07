#!/usr/bin/python3
import json
"""
A function that writes an Object to a text file, using a JSON representation
"""


def save_to_json_file(my_obj, filename):
    """
    An object to a text file using its JSON representation

    Args:
        my_obj: The object to be serialized to JSON.
        filename (str): The name of the file to write the JSON representation

    Returns:
        None
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
