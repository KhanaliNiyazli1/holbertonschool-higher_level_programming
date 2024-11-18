#!/usr/bin/python3
def islower(c):
    return (ord('a') <= ord(c) <= ord('z')) and isinstance(c, str) and len(c) == 1
