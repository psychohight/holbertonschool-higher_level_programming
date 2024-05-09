#!/usr/bin/python3
print(''.join(chr(letter) for letter in range(97, 123) if letter != 101 and letter != 113).format(), end='')
