#!/usr/bin/env python3

# Usage <scriptname.py> <integer>

'''
Improved version, avoids endless recurison using base cases just
as version 2 did, but now includes memoisation to prevent needless
recalculation through the recursive cycle.'''

import sys
from typing import Dict

# Takes passed argument
n = int(sys.argv[1])

# Use memoisation
memo: Dict[int, int] = {0:0, 1:1}           # base cases


def fib(n: int) -> int:
    if n not in memo:
        memo[n] = fib(n - 1) + fib(n - 2)   # memoisation and recursion
    return memo[n]

def main():
    if __name__ == "__main__":
        print(fib(n))
main()