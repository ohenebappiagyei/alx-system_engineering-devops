#!/usr/bin/python3
"""
This is the function that returns the JSON representation of an object
"""
import json


def to_json_string(my_obj):
    """
    Return the JSON representation of an object as a string.

    Args:
        my_obj: The object to be serialized to JSON.

    Returns:
        str: The JSON representation of the object as a string.
    """
    return json.dumps(my_obj)
