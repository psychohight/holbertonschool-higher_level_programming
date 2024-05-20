#!/usr/bin/python3
class Square:

    def __init__(self, size=0):

        if not isinstance(size, int):
            raise TypeError
        elif size < 0:
            raise ValueError
        else:
            self.__size = size

    def area(self):

        return (self.__size ** 2)
