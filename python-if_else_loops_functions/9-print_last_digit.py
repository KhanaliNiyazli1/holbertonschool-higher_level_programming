#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10
    if last_digit < 0:
        last_digit = -last_digit
