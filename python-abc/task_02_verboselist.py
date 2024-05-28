#!/usr/bin/env python3
from typing import Iterable, SupportsIndex

class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added {item} to the list.")

    def extend(self, iterable):
        super().extend(iterable)
        print(f"Extended the list with {len(iterable)} items.")
    
    def remove(self, item):
        super().remove(item)
        print(f"Removed {item} from the list.")

    def pop(self, index=-1):
        item = super().pop(index)
        print(f"“Popped {index} from the list.")
        return item