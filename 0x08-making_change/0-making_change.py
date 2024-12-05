#!/usr/bin/python3
"""
A function to determine the fewest number of coins
"""

def makeChange(coins, total):
    """Given a pile of coins of different values"""
    
    # If total is 0 or negative, return 0 as no coins are needed
    if total <= 0:
        return 0

    # Initialize a dp array where dp[i] is the minimum number of coins needed to make amount i
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make amount 0

    # Iterate through each coin
    for coin in coins:
        # Update the dp array for each possible amount from the coin value to total
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, it's not possible to make the total with the given coins
    return dp[total] if dp[total] != float('inf') else -1
