!/usr/bin/python3
"""
This is a function that appends a string at the end of a text file
(UTF-8) and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    Append a string to the end of a text file (UTF-8) and return
    the number of characters added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to be appended to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        num_characters_added = file.write(text)
    return num_characters_added