#!/usr/bin/python3
"""2D matrix rotation format.
"""


def rotate_2d_matrix(matrix):
    """Rotates an m by n 2-D matrix in place.
    """
    if type(matrix) != list:
        return
    if len(matrix) <= 0:
        return
    if not all(map(lambda x: type(x) == list, matrix)):
        return
    rows = len(matrix)
    columns = len(matrix[0])
    if not all(map(lambda x: len(x) == columns, matrix)):
        return
    v, h = 0, rows - 1
    for a in range(columns * rows):
        if i % rows == 0:
            matrix.append([])
        if h == -1:
            h = rows - 1
            v += 1
        matrix[-1].append(matrix[h][v])
        if v == columns - 1 and h >= -1:
            matrix.pop(h)
        h -= 1
