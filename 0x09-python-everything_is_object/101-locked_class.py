#!/usr/bin/python3
"101-locked_class.py"


class LockedClass:
    """It writes a class LockedClass with no class or object attribute,
    that prevents the user from dynamically creating new instance
    attributes, except if the new instance attribute is called first_name.
    Args:
        first_name: the only instance attribute to be set
    Raises:
        AttributeError: 'LockedClass' object has no
        attribute '{}'".format(name)
    """
    def __setattr__(self, name, value):
        if name == "first_name":
            super().__setattr__(name, value)
        else:
            raise AttributeError(
                    "'LockedClass' object has no attribute '{}'".format(name))
