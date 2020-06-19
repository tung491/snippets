"""
Flatten a n-D list (n > 2) to 1-D list using recursion
"""


def flatten(input_list: list) -> list:
    """
    Flatten child elements of elements to 1-D list
    if this elements is list, tuple or set
    :param input_list: list
    :return: list
    """
    if not input_list:
        return []
    head, *tail = input_list
    is_iterator = any(isinstance(head, type_) for type_ in [list, tuple, set])
    if is_iterator:
        return flatten(head) + flatten(tail)
    return [head] + flatten(tail)


def main() -> None:
    print(flatten([1, [2, [3, 4]]]))
    print(flatten([1, (2, 3, {4, 5})]))


if __name__ == '__main__':
    main()
