#!/usr/bin/python3
"""
Student class with a method that returns a filtered dictionary
representation of its attributes.
"""


class Student:
    """
    Defines a student with first_name, last_name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize the student with first name, last name, and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the Student.
        If attrs is a list of strings, returns only those attributes.
        Otherwise, returns all attributes.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
