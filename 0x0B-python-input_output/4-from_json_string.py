#!/usr/bin/python3
"""
This is a function that returns an object (Python data structure)
represented by a JSON string
"""
import json


def from_json_string(my_str):
    """
    Return a Python data structure (object) represented by a JSON string.

    Args:
        my_str (str): The JSON string to be deserialized.

    Returns:
        object: The python data structure represented by the JSON string.
    """
    return json.loads(my_str)
