#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    
    max_a = my_list[0]
    for i in my_list:
        if i > max_a:
            max_a = i

    return max_a
