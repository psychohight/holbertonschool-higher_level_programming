#!/usr/bin/python3

class Square:
    """ A class defines a square by its size
    """
    def __init__(self, size=0):
        """ initialize the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)

    def area(self):
        """ returns the square
        """
        return (self.__size ** 2)