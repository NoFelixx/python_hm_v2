"""
Given a cell with "it's a fib sequence" from slideshow,
please write function "check_fib", which accepts a Sequence of integers, and
returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from collections.abc import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    if len(data) < 2:
        return False

    prev, curr = 0, 1
    for i in range(2, len(data)):
        if data[i] != prev + curr:
            return False
        prev, curr = curr, data[i]

    return True


a = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print(check_fibonacci(a))
