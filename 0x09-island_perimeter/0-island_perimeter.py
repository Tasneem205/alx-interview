#!/usr/bin/python3
"""ialsnd problem solution file"""


def island_perimeter(grid):
    """function to cal island perimeter"""
    peri = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if i == 0 or grid[i-1][j] == 0:
                    peri += 1
                if i == len(grid)-1 or grid[i+1][j] == 0:
                    peri += 1
                if j == 0 or grid[i][j-1] == 0:
                    peri += 1
                if j == len(grid[i])-1 or grid[i][j+1] == 0:
                    peri += 1
    return peri
