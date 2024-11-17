#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:  # Add space around the operator
    print(f"{number} is positive")
elif number < 0:  # Add space around the operator
    print(f"{number} is negative")
else:
    print(f"{number} is zero")
