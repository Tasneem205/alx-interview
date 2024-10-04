#!/usr/bin/python3
"""
define pascal triangle in a string format
"""


def pascal_triangle(n):
    """ function to return list of lists of pascal tri """
    tri = []
    str1 = [1]
    str2 = []
    tri.append(str1)
    if type(n) is not int or n <= 0:
        return []
    for _ in range(1, n):
        for i in range(0, len(str1) + 1):
            if i == 0 or i == len(str1):
                str2.append(str1[0])
            else:
                str2.append(str1[i] + str1[i-1])
        tri.append(str2)
        str1 = str2
        str2 = []
    return tri
