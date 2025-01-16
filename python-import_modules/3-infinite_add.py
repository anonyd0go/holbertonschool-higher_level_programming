#!/usr/bin/python3
import sys

if __name__ == "__main__":
    sum = 0
    for i in range(1, len(sys.argv)):
        try:
            sum += int(sys.argv[i])
        except ValueError:
            continue
    print(sum)
    