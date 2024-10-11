#!/usr/bin/python3


def canUnlockAll(boxes):
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = [0]  # Start with the first box's keys
    
    while keys:
        key = keys.pop()
        for new_key in boxes[key]:
            if new_key < n and not unlocked[new_key]:
                unlocked[new_key] = True
                keys.append(new_key)

    return all(unlocked)
