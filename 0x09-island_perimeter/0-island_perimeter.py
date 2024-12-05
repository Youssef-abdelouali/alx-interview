#!/usr/bin/python3
"""
This module defines the island_perimeter function.
"""

def island_perimeter(grid):
    """
    Calculates the perimeter of an island in a grid.

    Args:
        grid (list of list of int): A 2D grid representing the map where
                                    0 = water, 1 = land.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Land cell
                # Assume 4 sides contribute to the perimeter initially
                perimeter += 4
                
                # Check for adjacent land cells to subtract shared sides
                if i > 0 and grid[i - 1][j] == 1:  # Land cell above
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:  # Land cell to the left
                    perimeter -= 2

    return perimeter
