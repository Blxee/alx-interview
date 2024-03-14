#!/usr/bin/python3
"""Module for Primegame solution."""


def isWinner(x, nums):
    """Determines the winner in Primegame."""
    winner = 0
    for num in nums:
        primes = sieve_of_eratosthenes(num)
        if len(primes) % 2 == 0:
            winner += 1
        else:
            winner -= 1
    if winner > 0:
        return 'Ben'
    elif winner < 0:
        return 'Maria'
    else:
        return None


def sieve_of_eratosthenes(num):
    """Retrieves all prime number between 2 and num."""
    lst = list(range(1, num + 1))
    for i in range(1, len(lst)):
        if lst[i] == 0:
            continue
        for j in range(i + lst[i], len(lst), lst[i]):
            lst[j] = 0
        if lst[i] ** 2 >= num:
            break
    return [i for i in lst if i != 0][1:]
