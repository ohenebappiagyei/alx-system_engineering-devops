#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    total_sum = 0

    if len(argv) > 1:  # Check if there are arguments
        for i in range(1, len(argv)):  # Start from index 1 to skip the script name
            total_sum += int(argv[i])

        print("{}".format(total_sum))
    else:
        print("0")

