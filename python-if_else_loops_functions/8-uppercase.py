#!/usr/bin/python3
def uppercase(str):
    result = ""  # Initialize an empty string to collect the result
    for i in str:
        if ord('a') <= ord(i) <= ord('z'):
            result += chr(ord(i) - 32)  # Convert to uppercase
        else:
            result += i  # Keep the character as-is if not lowercase

    print("{}".format(result))  # Print the final result (no trailing space)
