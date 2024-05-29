#!/usr/bin/python3

def read_file(filename=""):
    """Reads a text file (UTF8) and prints it
    """
    with open(filename, "r", encoding='utf-8') as file:
        content = file.read()
        print(content, end="")