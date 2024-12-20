#!/usr/bin/python3
"""
unlock boxes interview question
"""


def canUnlockAll(boxes):
    """
    return true if possible false otherwise
    """
    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False
    opened = 0
    visited = [False] * len(boxes)
    q = []
    q.extend(boxes[0])
    opened += 1
    visited[0] = True
    for i in q:
        if i < len(boxes) and not visited[i]:
            visited[i] = True
            opened += 1
            q.extend(boxes[i])

    if opened == len(boxes):
        return True
    return False
