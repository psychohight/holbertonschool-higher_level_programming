#!/usr/bin/env python3
"""
My file is commented
"""


def class_to_json(obj):
    """Return the dictionary representation
    """
    obj_dict = {}

    for attr in dir(obj):
        if not attr.startswith('__') and not attr.endswith('__'):
            value = getattr(obj, attr)

            if isinstance(value, (list, dict, str, int, bool)):
                obj_dict[attr] = value
    
    return obj_dict
