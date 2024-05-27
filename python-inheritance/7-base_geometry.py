#!/usr/bin/python3
""" BaseGeometry Class """
class BaseGeometry:
    """ BaseGeometry Class """
    def area(self):
        """ Area Method """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """ Integer Validator Method """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")