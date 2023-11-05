#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]  # Get the command-line arguments, excluding the script name
    num_args = len(args)  # Get the number of arguments

    print(f"{num_args} {'argument' if num_args == 1 else 'arguments'}:", end="")
    print("." if num_args == 0 else ":")
    
    for i in range(num_args):
        print(f"{i + 1}: {args[i]}")

