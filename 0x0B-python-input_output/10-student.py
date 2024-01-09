#!/usr/bin/python3
"""10-student module"""


class Student:
    """A class Student that defines a student"""
    def __init__(self, first_name, last_name, age):
        """The class constructor.
        Args:
            first_name: the first name of te student
            last_name: the last name of te student
            age: the age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Public method that retrieves a dictionary representation
        of a Student instance.
        """
        result = {}
        if attrs is None:
            for key in self.__dict__:
                result[key] = getattr(self, key)
        else:
            for key in attrs:
                if hasattr(self, key):
                    result[key] = getattr(self, key)
        return result
