#!/usr/bin/env python3

# Usage <scriptname.py> <integer>

'''
Moving from recursion to iteration.'''

import sys

# Takes passed argument
n = int(sys.argv[1])

# Use of decorator function for caching
def fib(n: int) -> int:
    if n == 0:
        return n  # Special case
    last: int = 0 # Set initial 
    next: int = 1 # Set initial
    for _ in range(1, n):
        last, next = next, last + next
    return next

def main():
    if __name__ == "__main__":
        print(fib(n))
main()