#!/usr/bin/env python3

# Usage <scriptname.py> <integer>

'''
Initial version of the Fibonacci script - built with flaws to demonstrate
how "valid code" can still cause problems at execution.'''

# Takes an argument at run time, but fails due to infinite regression.

import sys

n = int(sys.argv[1])

def fib(n: int) -> int:
    return fib(n - 1) + fib(n - 2)

def main():
    if __name__ == "__main__":
        print(fib(n))
main()