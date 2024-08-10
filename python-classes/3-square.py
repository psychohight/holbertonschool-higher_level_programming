#!/usr/bin/python3
"""
My file is commented
"""
class Square:
    """ A class defines a square by its size
    """
    def __init__(self, size=0):
        """ initialize the square
        """
        if not isinstance(size, int):
            raise TypeError
        elif size < 0:
            raise ValueError
        else:
            self.__size = size

    def area(self):
        """ returns the square
        """
        return (self.__size ** 2)