#!/usr/bin/python3
def islower(c):
    if not isinstance(c, str) or len(c) != 1:
        return ord('a') <= ord(c) <= ord('z') and isinstance(c, str) and len(c) == 1
