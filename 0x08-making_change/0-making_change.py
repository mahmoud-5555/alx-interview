#!/usr/bin/python3
""" This module is a solution for the Making Change problem. """


def makeChange(coins, total):
    """
    Returns the minimum number of coins needed to
      make change for the given total.
      """
    if total <= 0:
        return 0

    dp = [0]
    max_value = total + 1
    for i in range(1, total + 1):
        dp.append(max_value)
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != total + 1 else -1
