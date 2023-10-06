#!/usr/bin/python3
""" task 0
"""


def canUnlockAll(boxes):
    """determines if all the boxes can be opened.
    """
    if not boxes:
        return False

    n = len(boxes)
    visited = [False] * n
    visited[0] = True  # The first box is unlocked
    stack = [0]

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                stack.append(key)

    return all(visited)

