#!/usr/bin/python3
"""Module defining the Base class."""


import json


class Base:
    """The base class for all other classes in this project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constrctor for the Base class.

        Args:
            id (int): The unique identifier for the instance.
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of dictionaries from the JSON string representation.


        Args:
            json_string (str): JSON string representing a list of dictionaries.

        Returns:
            list: List of dictionaries.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as file:
            objs_as_dicts = [obj.to_dictionary() for obj in list_objs]
            json_str = cls.to_json_string(objs_as_dicts)
            file.write(json_str)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with all attributes already set.

        Args:
            **dictionary: Double pointer to a dictionary.

        Returns:
            Base: Instance with attributes set.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            raise ValueError("Unsupported class")

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from a JSON file.

        Returns:
            list: List of instances.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r', encoding="utf-8") as file:
                json_data = file.read()
                list_dict = cls.from_json_string(json_data)
                return [cls.create(**d) for d in list_dict]
        except FileNotFoundError:
            return []
