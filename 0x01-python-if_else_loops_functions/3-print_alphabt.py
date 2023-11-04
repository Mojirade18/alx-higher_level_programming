#!/usr/bin/python3

output = ""
for letter in range(97, 123):
    if chr(letter) not in 'qe':
        output += chr(letter)

print(output, end="\n")

