#!/usr/bin/python3
""" Rectangle Class that inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ Rectangle Class 
    BaseGeometry: BaseGeometry Class
    """
    def __init__(self, width, height):
        """ Rectangle Class 
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height