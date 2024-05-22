#!/usr/bin/python3
"""function that prints 2 new lines after ".?:" characters
"""
def text_indentation(text):
    """ Function that prints 2 new lines after ".?:" characters
    text: input string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    segments = []
    start = 0

    for i, char in enumerate(text):
        if char in '.?:':
            segments.append(text[start:i + 1].strip())
            start = i + 1

    if start < len(text):
        segments.append(text[start:].strip())
    
    print("\n\n".join(segments))