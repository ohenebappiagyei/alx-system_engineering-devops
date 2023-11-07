#!/usr/bin/python3
"""
A class 'Student' that defines a student
"""


def class_to_json(obj):
    """Return a dictionary description for JSON serialization of an object.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: A dictionary containing serializable attributes of the object. 
    """
    serializable_data = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serializable_data[key] = value
    return serializable_data
