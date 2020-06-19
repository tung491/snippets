"""
Flatten a n-D list (n > 2) using recursion
"""


def flatten(input_list: list) -> list:
    if not input_list:
        return []
    head, *tail = input_list
    is_iterable = any(isinstance(head, type_) for type_ in [list, tuple, set])
    if is_iterable:
        return flatten(head) + flatten(tail)
    return [head] + flatten(tail)


def main():
    print(flatten([1, [2, [3, 4]]]))
    print(flatten([1, (2, 3, {4, 5})]))


if __name__ == '__main__':
    main()
