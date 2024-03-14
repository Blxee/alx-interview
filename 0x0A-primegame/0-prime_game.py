#!/usr/bin/python3


def isWinner(x, nums):
    for num in nums:
        primes = sieve_of_eratosthenes(num)
        if len(primes) % 2 == 0:
            return 'Ben'
        else:
            return 'Maria'


def sieve_of_eratosthenes(num):
    lst = list(range(1, num + 1))
    for i in range(1, len(lst)):
        if lst[i] == 0:
            continue
        for j in range(i + lst[i], len(lst), lst[i]):
            lst[j] = 0
        if i ** 2 >= num:
            break
    return [i for i in lst if i != 0]
