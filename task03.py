"""
Write down the function, which reads input line-by-line, and find maximum and minimum values.
Function should return a tuple with the max and min values.

For example for [1, 2, 3, 4, 5], function should return [1, 5]

We guarantee, that file exists and contains line-delimited integers.

To read file line-by-line you can use this snippet:

with open("some_file.txt") as fi:
for line in fi:

"""
from typing import Tuple


def find_maximum_and_minimum() -> Tuple[int, int]:
    max_val = float('-inf')
    min_val = float('inf')

    with open("note.txt") as fi:
        for line in fi:
            val = int(line)
            max_val = max(max_val, val)
            min_val = min(min_val, val)

    return max_val, min_val


print(find_maximum_and_minimum())
