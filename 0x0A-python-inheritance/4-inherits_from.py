#!/usr/bin/python3
"""4-inherits_from module"""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class
    that inherited (directly or indirectly) frm the specified
    class ; otherwise False
    """

    if isinstance(obj, a_class) and (type(obj) is not a_class):
        return True
    else:
        return False
