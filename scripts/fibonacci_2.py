#!/usr/bin/env python3

# Usage <scriptname.py> <integer>

'''
Improved version, avoids endless recurison using base cases
Still is not optimal for O(n) purposes - it recalculates for
every turn of the wheel through each number in the sequence.
We should optimise in the next version so results are cached.'''

import sys

n = int(sys.argv[1])

def fib(n: int) -> int:
    if n <2:                        # base case
        return n
    return fib(n - 1) + fib(n - 2)  # recursive case

def main():
    if __name__ == "__main__":
        print(fib(n))
main()