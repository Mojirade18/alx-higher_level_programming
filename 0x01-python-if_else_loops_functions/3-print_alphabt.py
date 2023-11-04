#!/usr/bin/python3

for letter in range(97, 123):
    if chr(letter) not in 'qe':
        print("{}".format(chr(letter), end=''), end='')

print()  # Add a newline at the end to match the desired output

