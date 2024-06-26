#!/usr/bin/python3
import json

def save_to_json_file(my_obj, filename):
    """Writes an object to a text file (JSON representation)
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))