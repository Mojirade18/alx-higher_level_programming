#!/usr/bin/python3
# Author: MOJIRADE OLURANTI

output = ""
for letter in range(97, 123):
    if chr(letter) not in 'qe':
        output += chr(letter)

print(output, end="")
print()  # Add a newline at the end to match the desired output

