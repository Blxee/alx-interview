#!/usr/bin/python3
"""0. Minimum Operations"""


def minOperations(n):
    """Determines the minimum number of operations to write H n times.

    Args:
        n (int): number of H characters to achieve.
    Returns:
        int: minimum number of operations, or 0.
    """
    if n <= 1:
        return 0
    op = 2
    while n % op != 0:
        op += 1
    return op + minOperations(int(n / op))
