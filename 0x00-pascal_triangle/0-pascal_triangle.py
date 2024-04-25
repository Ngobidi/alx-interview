#!/usr/bin/python3
"""draft A module determine pascal's triangle of a given number"""

def pascal_triangle(n):
    """
    draft and display a list of lists of integers representing the Pascal’s triangle of n
    """
    triangle = []
    if type(n) is not int or n <= 0:
        return triangle
    for a in range(n):
        line = []
        for b in range(a + 1):
            if b == 0 or b == i:
                line.append(1)
            elif a > 0 and b > 0:
                line.append(triangle[a - 1][b - 1] + triangle[a - 1][b])
        triangle.append(line)
    return triangle
