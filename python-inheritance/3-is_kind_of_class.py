#!/usr/bin/python3
"""Defines a function that returns True if the object is an instance
"""
def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance
    otherwise False.
    """
    if isinstance(obj, a_class):
        return True
    return False