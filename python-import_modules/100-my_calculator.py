#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    if argv[2] == '+':
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif argv[2] == '-':
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif argv[2] == '*':
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    elif argv[2] == '/':
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
