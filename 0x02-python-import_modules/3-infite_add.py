#!/usr/bin/python

from sys import argv


def calculate_sum_of_arguments():
    # Initialize the sum to 0
    total_sum = 0

    # Iterate through the arguments and a dd them to the total sum
    for i in range(1, len(sys.argv)):
        total_sum += int(sys.argv[i])

    # Print the total sum
    print("{}".format(total_sum))


if __name__ == "__main__":
    calculate_sum_of_arguments()
