#!/usr/bin/python3
"""ialsnd problem solution file"""


def island_perimeter(grid):
    """function to cal island perimeter"""
    peri = 0
    for i in range(0,len(grid)):
        for j in range(0, len(grid[i])):
            if i == 0 and grid[i][j] == 1:
                peri += 1
            elif i == len(grid)-1 and grid[i][j] == 1:
                peri += 1
            elif grid[i-1][j] != grid[i][j]:
                peri += 1

            if j == 0 and grid[i][j] == 1:
                peri += 1
            elif j == len(grid[i])-1 and grid[i][j] == 1:
                peri += 1
            elif grid[i][j-1] != grid[i][j]:
                peri += 1
    return peri
