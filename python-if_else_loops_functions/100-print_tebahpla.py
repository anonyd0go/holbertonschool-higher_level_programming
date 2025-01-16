#!/usr/bin/python3
for i in range(25, -1, -1):
    if i % 2 == 1:
        print("{:c}".format(i + 97), end="")
    else:
        print("{:c}".format(i + 65), end="")
