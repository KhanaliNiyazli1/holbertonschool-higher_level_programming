#!/usr/bin/python3
def islower(c):
    if not isinstance(c, str) or len(c) != 1:
        return False
    return ord('a') <= ord(c) <= ord('z')