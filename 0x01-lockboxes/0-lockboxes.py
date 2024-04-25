#!/usr/bin/python3
"""A python module for working with lockboxes.
"""


def canUnlockAll(boxes):
    """valiates a module that returns if True, all box in
    boxes can be opened
    """
    n = len(boxes)
    seen_boxes = set([0])
    unseen_boxes = set(boxes[0]).difference(set([0]))
    while len(unseen_boxes) > 0:
        box-Idx = unseen_boxes.pop()
        if not box-Idx or box-Idx >= n or box-Idx < 0:
            continue
        if box-Idx not in seen_boxes:
            unseen_boxes = unseen_boxes.union(boxes[box-Idx])
            seen_boxes.add(box-Idx)
    return n == len(seen_boxes)
"""
