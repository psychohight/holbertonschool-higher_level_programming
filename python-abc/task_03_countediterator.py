#!/usr/bin/env python3

class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        return self.count
    
    def __next__(self):
        self.count += 1
        item = next(self.iterator)
        return item
        StopIteration

    