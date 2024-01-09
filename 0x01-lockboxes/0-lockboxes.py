#!/usr/bin/python3
"""0. Lockboxes"""


def canUnlockAll(boxes: list[list[int]]) -> bool:
    """determines if all the boxes can be opened.

    Args:
        boxes (list[list[int]]): list of boxes contaning keys

    Returns:
        bool: True if all boxes can be opened, else return False.
    """
    if len(boxes) <= 1:
        return True

    keys = {0}
    locked = set(range(len(boxes)))
    while True:
        ended = True
        for key in keys.copy():
            if key in range(len(boxes)):
                keys.update(boxes[key])
                if key in locked:
                    locked.remove(key)
                    ended = False
        if ended:
            break

    if len(locked) == 0:
        return True
    else:
        return False
