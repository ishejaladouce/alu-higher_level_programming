#!/usr/bin/python3
"""
This module defines a Student class with methods to serialize
and reload attributes from a dictionary.
"""


class Student:
    """
    Defines a student with first_name, last_name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the Student.
        If attrs is a list of strings, returns only matching keys.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str)
                                           for attr in attrs):
            return {
                k: getattr(self, k) for k in attrs if hasattr(self, k)
            }
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student using a dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
