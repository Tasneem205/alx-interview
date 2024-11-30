#!/usr/bin/python3
"""
making change function file
"""


def makeChange(coins, total):
    """Find the minimum number of coins needed to make the total."""
    if total <= 0:
        return 0
    coins = set(coins)

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1

    return dp[total] if dp[total] != float('inf') else -1
