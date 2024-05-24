#!/usr/bin/python3
"""class rectangle
"""

class Rectangle:
    """create a private instance
        
        width: horizontal 
        height: vertical 
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances +=1

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

    def area(self):
        """Calculates area
        
        Return: area
        """
        return self._width * self._height

    def perimeter(self):
        """Calculates perimeter
        
        Returns: perimeter
        """
        if self._width == 0 or self._height == 0:
            return 0
        return 2 * (self._width + self._height)
    
    def __str__(self):
        """Returns a string
        
        Returns: string
        """
        if self._width == 0 or self._height == 0:
            return ""
        symbol = str(self.print_symbol)
        return "\n".join([symbol * self._width for _ in range(self._height)])

    def __repr__(self):
        """Return a string representation
        
        Returns: String representation
        """
        return "Rectangle({}, {})".format(self._width, self._height)
    
    def __del__(self):
        """Print a message
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -=1