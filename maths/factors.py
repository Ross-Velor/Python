from doctest import testmod
from math import isqrt


def factors_of_a_number(num: int) -> list[int]:
    """
    Return all positive integer factors of a number in ascending order.

    >>> factors_of_a_number(1)
    [1]
    >>> factors_of_a_number(5)
    [1, 5]
    >>> factors_of_a_number(24)
    [1, 2, 3, 4, 6, 8, 12, 24]
    >>> factors_of_a_number(0)
    []
    >>> factors_of_a_number(-24)
    []
    """
    if num < 1:
        return []

    facs: list[int] = []
    for i in range(1, isqrt(num) + 1):
        if num % i == 0:
            facs.append(i)
            d = num // i
            if d != i:
                facs.append(d)

    facs.sort()
    return facs


if __name__ == "__main__":
    testmod(verbose=True)
