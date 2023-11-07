#!/usr/bin/python3
"""
This is a function that reads a text file(UTF-8) and prints it to stdout
"""


def read_file(filename=""):
    """Read and print the content of a text file.

    Args:
        filename (str): The name of the file to read.


    Returns:
        None
    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
