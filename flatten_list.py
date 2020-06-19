"""
Flatten a n-D list (n > 2) to 1-D list using recursion
"""


def flatten(input_list: list) -> list:
    """
    Flatten all child elements of inner element
    if that is list, tuple or set
    :param input_list: list
    :return: list
    """
    if not input_list:
        return []
    head, *tail = input_list
    if isinstance(head, (list, tuple, set)):
        return flatten(head) + flatten(tail)
    return [head] + flatten(tail)


def main() -> None:
    print(flatten([1, [2, [3, 4]]]))
    print(flatten([1, (2, 3, {4, 5})]))


if __name__ == '__main__':
    main()
