#!/usr/bin/python3
"""1-my_list module"""


class MyList(list):
    """a class MyList that inherits list"""
    def print_sorted(self):
        """prints the list, but sorted (ascending sort)
        Raises:
            ValueError: Input is not a list.
            ValueError: Input must be a list of numbers.
        """

        if not isinstance(self, list):
            raise ValueError("Input is not a list.")

        if not all(isinstance(x, int) for x in self):
            raise ValueError("Input must be a list of numbers.")

        if None in self:
            raise ValueError("Input must be a list of numbers.")

        self = sorted(self)
        print(self)
