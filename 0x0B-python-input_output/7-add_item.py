#!/usr/bin/python3
import sys
import os

# Import your save_to_json_file and load_from_json_file functions
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item_to_list(item, filename):
    """
    Add an item to a list and save the list as a JSON representation in a file.

    Args:
        item (str): The item to be added to the list.
        filename (str): The name of the file to save the list in.

    The function loads the existing list from the file
      if it exists or initializes an empty list if the file doesn't exist.
    It appends the provided item to the list
      and saves the updated list as a JSON representation in the file.

    The function doesn't handle file permissions or exceptions.
    """
    # Initialize an empty list if the file doesn't exist
    if not os.path.exists(filename):
        item_list = []
    else:
        # Load the existing list from the file
        item_list = load_from_json_file(filename)

    # Add the command-line argument to the list
    item_list.append(item)

    # Save the updated list as a JSON representation in the file
    save_to_json_file(item_list, filename)
