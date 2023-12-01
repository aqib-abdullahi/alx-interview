#!/usr/bin/python3
"""makeChange module
"""

def makeChange(coins, total):
    """determine the fewest number of coins
    needed to meet a given amount total.
    """
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0
    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                min_coins[amount] = min(min_coins[amount], min_coins[amount - coin] + 1)
    if min_coins[total] == float('inf'):
        return -1
    else:
        return min_coins[total]

