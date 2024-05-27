#!/usr/bin/python3
""" Square Class inherits from Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """ Square Class 
    Rectangle: Rectangle Class
    """
    def __init__(self, size):
        """ Square Class 
        """
        self.integer_validator("size", size)
        super().__init__(size, size)