"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.

You may assume that the array is non-empty and the most common element
always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3, 2

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2, 1

"""
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    count_dict = {}
    for elem in inp:
        if elem not in count_dict:
            count_dict[elem] = 1
        else:
            count_dict[elem] += 1
    most_common = max(count_dict, key=count_dict.get)
    least_common = min(count_dict, key=count_dict.get)
    return most_common, least_common
