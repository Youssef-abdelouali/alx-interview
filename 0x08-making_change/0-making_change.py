#!/usr/bin/python3

def makeChange(coins, total):
    # If total is less than or equal to 0, no coins are needed
    if total <= 0:
        return 0

    # Initialize the dp array with a large number (infinity)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make total 0

    # Iterate over each coin denomination
    for coin in coins:
        for i in range(coin, total + 1):
            # For each value from coin to total, calculate the minimum coins needed
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, it means the total cannot be made with the given coins
    return dp[total] if dp[total] != float('inf') else -1
