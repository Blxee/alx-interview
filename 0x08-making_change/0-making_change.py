#!/usr/bin/python3
"""Module for task 0. Change comes from within"""


def makeChange(coins, total):
    """Solution for coin change problem"""
    coins.sort(reverse=True)
    count = 0
    while total > 0:
        if len(coins) == 0:
            return -1
        if total < coins[0]:
            coins.pop(0)
            continue
        total -= coins[0]
        count += 1
    return count
