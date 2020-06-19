"""
Check if all elements in iterable is unique
Time Complexity: O(n)
Space Complexity: O(n)
"""
from typing import Iterator
from collections import defaultdict


def check_unique(input_iterable: Iterator) -> bool:
    """
    :param input_iterable: Iterator
    :return: bool
    Return True if all elements in input_iterator is unique, otherwise return False
    """
    exists = defaultdict(bool)

    for x in input_iterable:
        if exists[x]:
            return False
        exists[x] = True
    return True


def main() -> None:
    print(check_unique('aba'))
    print(check_unique(range(10)))
    print(check_unique('abc'))


if __name__ == '__main__':
    main()
