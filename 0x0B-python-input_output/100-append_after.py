#!/usr/bin/python3
"""
A function that inserts a line of text to a file, after each line
containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text after each line containing a specific string
    in a file.

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The string to search for in each line of the file.
        new_string (str): The line of text to insert after each line
        containing the search string.

    This function doesn't handle file permission or file not existing exception
    """
    lines_to_write = []

    with open(filename, 'r') as file:
        for line in file:
            lines_to_write.append(line)
            if search_string in line:
                lines_to_write.append(new_string)

    with open(filename, 'w') as file:
        file.writelines(lines_to_write)
