#!/usr/bin/python3
"""
This is a script that adds all arguments to a Python list,
 and then save them to a file.
"""


import sys
from os.path import exists
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

def add_item(filename, *args):
    """Add arguments to a Python list and save them to a JSON file.
    
    Args:
        filename (str): The name of the JSON file.
        args: Variable number of arguments to add to the list.

    Returns:
        None
    """
    if exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    my_list.extend(args)
    save_to_json_file(my_list, filename)
