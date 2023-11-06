#!/usr/bin/python3

"""This is program defines a function that returns a list of 
available attributes and methods of an object"""

def lookup(obj):
    """
    This function returns a list of available attributes and methods of an object.

    @obj: The object for which we want to retrieve attributes and methods.
    return: A list of strings, where each string is an attribute or method
            name of the object.
    """
    return dir(obj)
