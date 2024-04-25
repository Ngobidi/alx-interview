#!/usr/bin/python3
"""module for making_change.
"""


def makeChange(coins, total):
    """evaluates the fewest num of coins needed to meet a given
    amount total when given a pile of coins of different values.
    """
    if total <= 0:
        return 0
    bal = total
    coins_count = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while bal > 0:
        if coin_idx >= n:
            return -1
        if bal - sorted_coins[coin_idx] >= 0:
            bal -= sorted_coins[coin_idx]
            coins_count += 1
        else:
            coin_idx += 1
    return coins_count
