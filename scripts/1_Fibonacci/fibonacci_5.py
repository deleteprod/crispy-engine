#!/usr/bin/env python3

# Usage <scriptname.py> <integer>

'''
Improved version, avoids endless recurison using base cases just
as version 2 did, but now includes memoisation to prevent needless
recalculation through the recursive cycle. As an improvement over
version 3, this includes automatic memoisation.'''

import sys
from typing import Dict
from functools import lru_cache

# Takes passed argument
n = int(sys.argv[1])

# Use of decorator function for caching
@lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n <2:
        return n                    # base case
    return fib(n - 2) + fib(n - 1)  # recursive case

def main():
    if __name__ == "__main__":
        print(fib(n))
main()