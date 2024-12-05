# Coin Change Problem - Minimum Coins

This project implements a solution to the **Coin Change Problem**, where the objective is to determine the fewest number of coins needed to make a given total amount, given a list of coin denominations. This problem is commonly solved using **greedy algorithms** or **dynamic programming**.

## Problem Statement

Given a list of coin denominations and a total amount, determine the fewest number of coins needed to make the total amount. If it is not possible to make the total amount with the given coins, return `-1`.

### Function Prototype

```python
def makeChange(coins, total):
    """
    Arguments:
    coins (list of integers): A list of coin denominations you have.
    total (integer): The target amount to be achieved using the given coins.

    Returns:
    Integer: The fewest number of coins needed to meet the total.
             If total <= 0, return 0.
             If it is not possible to form the total using the given coins, return -1.
    """


