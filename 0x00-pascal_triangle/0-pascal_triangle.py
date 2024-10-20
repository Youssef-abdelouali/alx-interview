#!/usr/bin/python3
"""
0. Pascal's Triangle
"""


def pascal_triangle(n):
    """Create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n
    """
    re_s = []
    if n > 0:
        for i in range(1, n + 1):
            le_vel = []
            C_ = 1
            for j in range(1, i + 1):
                le_vel.append(C_)
                C_ = C_ * (i - j) // j
            re_s.append(le_vel)
    return re_s
