#!/usr/bin/python3
"""module for cumputing Island_perimeter.
"""


def island_perimeter(grid):
    """calculates the perimeter of an island with no lakes.
    """
    perimeter = 0
    if type(grid) != list:
        return 0
    n = len(grid)
    for x, row in enumerate(grid):
        m = len(row)
        for y, cell in enumerate(row):
            if cell == 0:
                continue
            edges = (
                x == 0 or (len(grid[x - 1]) > y and grid[x - 1][y] == 0),
                y == m - 1 or (m > y + 1 and row[y + 1] == 0),
                x == n - 1 or (len(grid[x + 1]) > y and grid[x + 1][y] == 0),
                y == 0 or row[y - 1] == 0,
            )
            perimeter += sum(edges)
    return perimeter
