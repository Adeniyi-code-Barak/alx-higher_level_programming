#!/usr/bin/python3
"""9-student module"""


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

    def to_json(self):
        """Public method that retrieves a dictionary representation
        of a Student instance.
        """
        if hasattr(self, '__dict__'):
            return self.__dict__
