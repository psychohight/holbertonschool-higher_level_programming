#!/usr/bin/python3
"""Module for inherits_from method.
"""
def inherits_from(obj, a_class):
    """inherits_from
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False