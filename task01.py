"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from typing import List
import string
from collections import Counter


def get_longest_diverse_words(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        text = file.read()
    words = text.translate(str.maketrans('', '', string.punctuation)).split()
    words = sorted(words, key=lambda w: len(set(w)), reverse=True)
    return words[:10]


def get_rarest_char(file_path: str) -> str:
    with open(file_path, 'r') as file:
        text = file.read()
    char_counts = Counter(text)
    return min(char_counts, key=char_counts.get)


def count_punctuation_chars(file_path: str) -> int:
    with open(file_path, 'r') as file:
        text = file.read()
    return sum(1 for char in text if char in string.punctuation)


def count_non_ascii_chars(file_path: str) -> int:
    with open(file_path, 'r') as file:
        text = file.read()
    return sum(1 for char in text if ord(char) > 127)


def get_most_common_non_ascii_char(file_path: str) -> str:
    with open(file_path, 'r') as file:
        text = file.read()
    non_ascii_chars = [char for char in text if ord(char) > 127]
    char_counts = Counter(non_ascii_chars)
    return max(char_counts, key=char_counts.get)
