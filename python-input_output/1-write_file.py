#!/usr/bin/python3
"""
My file is commented
"""
def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number of characters written
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)