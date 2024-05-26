#!/usr/bin/python3
"""Module for MyList class
"""
class MyList(list):
    """A class that inherits from list
    """
    def print_sorted(self):
        """Prints the list sorted."""
        print(sorted(self))