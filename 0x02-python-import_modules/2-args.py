#!/usr/bin/python3

import sys

def print_arguments():
    num_arguments = len(sys.argv) - 1

    # Print the number of arguments
    print("{} argument{}:".format(num_arguments, '' if num_arguments == 1 else 's'))

    # Print each argument and its position
    for i in range(1, num_arguments + 1):
        print("{}: {}".format(i, sys.argv[i]))

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("0 arguments.")
    else:
        print_arguments()
