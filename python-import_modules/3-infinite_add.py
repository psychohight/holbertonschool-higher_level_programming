#!/usr/bin/python3
import sys

def infinite_add():
    args = sys.argv[1:]
    total = 0

    for num in args:
        total += int(num)

    print(total)

if __name__ == "__main__":
    infinite_add()



