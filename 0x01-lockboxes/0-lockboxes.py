#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 and each
box may contain keys to the other boxes.
This module contains functions that determines if all the boxes can be opened
"""


def canUnlockAll(boxes):
    if not boxes:
        return True

    opened = set()
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        if current_box not in opened:
            opened.add(current_box)
            for key in boxes[current_box]:
                if key not in opened and key not in queue and key < len(boxes):
                    queue.append(key)

    return len(opened) == len(boxes)
