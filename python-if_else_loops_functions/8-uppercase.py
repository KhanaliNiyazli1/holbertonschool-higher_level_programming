#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord('a') <= ord(i) <= ord('z'):
            i = ord(i-32)
            print(i)
        else:
            print(i)
