#!/usr/bin/python3
def safe_print_division(a, b):
    result = None

    try:
        result = a / b
    except:
        result = None

    finally:
        print("inside result: {}".format(result))
        return result
