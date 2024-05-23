#!/usr/bin/python3
"""class rectangle
"""

class Rectangle:
    """create a private instance
        
        width: horizontal 
        height: vertical 
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """__width
        Returns: __width
        """
        return  self._width
    
    @width.setter
    def width(self, value):
        """value: horizontal value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """__height
        Returns: __height
        """
        return self._height
    
    @height.setter
    def height(self, value):
        """value: vertical value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value