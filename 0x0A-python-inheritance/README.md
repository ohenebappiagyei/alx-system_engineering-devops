# Python Inheritance Project

This Python project demonstrates the concept of object-oriented programming and inheritance in Python. It includes a set of classes that illustrate inheritance relationships and how to work with them.

## Table of Contents

- [Project Structure](#project-structure)
- [Classes](#classes)
- [How to Use](#how-to-use)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

The project is structured as follows:

- `1-lookup.py`: A Python script that defines a function to list attributes and methods of a given object.
- `2-is_same_class.py`: A Python script that defines a function to check if an object is an instance of a specified class.
- `3-is_kind_of_class.py`: A Python script that defines a function to check if an object is an instance of a class or a subclass of that class.
- `4-inherits_from.py`: A Python script that defines a function to check if an object is an instance of a class that inherited (directly or indirectly) from a specified class.
- `5-base_geometry.py`: A Python script that defines a `BaseGeometry` class with methods for integer validation.
- `6-base_geometry.py`: A Python script that defines a `BaseGeometry` class with an area method.
- `7-base_geometry.py`: A Python script that defines a `BaseGeometry` class with integer validation and a placeholder area method.
- `8-rectangle.py`: A Python script that defines a `Rectangle` class that inherits from `BaseGeometry`.
- `9-rectangle.py`: A Python script that defines a `Rectangle` class with private attributes, integer validation, an area method, and a string representation.
- `10-square.py`: A Python script that defines a `Square` class that inherits from `Rectangle`.
- `11-square.py`: A Python script that defines a `Square` class with size validation, an area method, and a string representation.
- `100-my_int.py`: A Python script that defines a `MyInt` class that inherits from `int` with inverted equality operators.
- `101-add_attribute.py`: A Python script that defines a function to add attributes to class instances if possible.

## Classes

- `BaseGeometry`: A base class that provides integer validation and an area method.
- `Rectangle`: A class that inherits from `BaseGeometry` and represents a rectangle with private attributes and methods.
- `Square`: A class that inherits from `Rectangle` and represents a square with size validation.

## How to Use

To use these classes and functions, you can import them into your Python scripts:

# Import other classes and functions as needed
