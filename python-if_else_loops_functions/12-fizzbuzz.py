#!/usr/bin/python3
def fizzbuzz():
    for i in range (101):
        if i % 3 == 0 and i % 5 == 0:
            return 'FizzBuzz'
        elif i % 3 == 0 and i % 5 != 0:
            return 'Fizz'
        elif i % 3 != 0 and i % 5 == 0:
            return 'Buzz'
        else:
            return i
