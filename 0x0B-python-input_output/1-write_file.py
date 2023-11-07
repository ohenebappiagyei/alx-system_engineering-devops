#!/usr/bin/python3
"""
This is a fucntion that writes a string to a text file (UTF-8)
and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF-8) and return the
    number of characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to be written to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        num_characters_written = file.write(text)
    return num_characters_written
