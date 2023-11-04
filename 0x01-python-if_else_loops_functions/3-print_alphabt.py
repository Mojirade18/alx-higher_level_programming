#!/usr/bin/python3

for letter in range(97, 123):
    if chr(letter) not in 'qe':
        print(chr(letter), end='')  # This single print statement without .format()

print()  # Add a newline at the end to match the desired output

