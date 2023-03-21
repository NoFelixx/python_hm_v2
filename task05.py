"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""
from typing import List, Any


def custom_range2(line, stop, start=None, step=None) -> List[Any]:
    if start is None and step is None:
        return line[:line.index(stop)]
    elif start is not None and step is not None:
        return line[line.index(start):line.index(stop):step]
    elif step is None and start is not None:
        return line[line.index(start):line.index(stop)]
    else:
        return line[:line.index(stop):step]
