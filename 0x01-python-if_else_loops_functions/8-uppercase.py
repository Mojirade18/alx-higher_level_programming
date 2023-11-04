#!/usr/bin/python3

def uppercase(s):
    for char in s:
        if ord('a') <= ord(char) <= ord('z'):
            # Convert lowercase character to uppercase using ASCII values
            upper_char = chr(ord(char) - ord('a') + ord('A'))
        else:
            upper_char = char
        print(upper_char, end='')
    print()  # Add a newline at the end

# Test the function with the provided code in 8-main.py
if __name__ == "__main__":
    uppercase("best")
    uppercase("Best School 98 Battery street")

