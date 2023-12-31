#!/usr/bin/python3

def print_last_digit(number):
    last_digit = abs(number) % 10  # Get the absolute value to handle negative numbers
    print(last_digit, end='')
    return last_digit

# Test the function with the provided code in 9-main.py
if __name__ == "__main__":
    print_last_digit(98)
    print_last_digit(0)
    r = print_last_digit(-1024)
    print(r)

