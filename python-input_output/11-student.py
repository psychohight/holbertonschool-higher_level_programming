#!/usr/bin/python3
"""
My file is commented
"""
class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return {
                    'first_name': self.first_name,
                    'last_name': self.last_name,
                    'age': self.age
                    }
        else:
            obj_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    obj_dict[attr] = getattr(self, attr)
            return obj_dict
        
    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)