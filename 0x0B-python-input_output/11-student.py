#!/usr/bin/python3
"""
A class 'Student' that defines a student
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance.

        Args:
            attrs (list, optional):
            A list of strings representing the attributes to retrieve.
                If None, all attributes will be retrieved.

        Returns:
            dict: A dictionary
            containing the specified attributes of the student.
        """
        if attrs is None:
            return self.__dict__
        return {
            attr: getattr(self, attr)
            for attr in attrs
            if hasattr(self, attr)
        }

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance with a dictionary.

        Args:
            json (dict): A dictionary
            containing attribute names and values to set.
        """
        for key, value in json.items():
            setattr(self, key, value)
