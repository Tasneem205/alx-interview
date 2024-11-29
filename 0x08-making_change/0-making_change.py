#!/usr/bin/python3
"""
making change function file
"""


def countRecur(coins, n, sum, memo):
    """Find the minimum number of coins and use memoization."""
    if sum == 0:
        return 0
    if sum < 0 or n == 0:
        return float('inf')

    if memo[n - 1][sum] != -1:
        return memo[n - 1][sum]

    include = 1 + countRecur(coins, n, sum - coins[n - 1], memo)
    exclude = countRecur(coins, n - 1, sum, memo)
    memo[n - 1][sum] = min(include, exclude)
    return memo[n - 1][sum]


def makeChange(coins, total):
    """Find the minimum number of coins needed to make the total."""
    if total <= 0:
        return 0

    memo = [[-1 for _ in range(total + 1)] for _ in range(len(coins))]
    result = countRecur(coins, len(coins), total, memo)

    return result if result != float('inf') else -1
