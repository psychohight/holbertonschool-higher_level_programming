#!/usr/bin/python3
"""
This module is composed by a function that adds two numbers
"""
def add_integer(a, b=98):
    """
    add two integer or float
    a: first nbr
    b: second nbr
    return: a + b
    """    
    if not isinstance(a, (int, float)):
        raise TypeError("a must be integer")
    
    if not isinstance(b, (int, float)):
        raise TypeError("b must be integer")
    
    return (int(a) + int(b))
