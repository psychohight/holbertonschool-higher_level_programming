#!/usr/bin/python3

def uppercase(str):
    for alph  in str:
        if 'a' <= alph <= 'z':
            c = chr(ord(alph) - 32)
        print("{}".format(alph), end="")
    print()
