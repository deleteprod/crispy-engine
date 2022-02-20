#!/usr/bin/env python3

# Usage <scriptname.py> <integer>

'''
Improved version, this time let's look at the use of
iteration instead of recursion. Remember that any 
problem that can be solved with recurison, can also
be solved with iteration'''

import sys

# Takes passed argument
n = int(sys.argv[1])

def fib(n: int) -> int:
    if n == 0: return n # our special case for early exit
    last: int = 0 # set starting
    next: int = 1 # more initialising of values
    for lol in range(1, n):
        last, next = next, last + next
    return next

def main():
    if __name__ == "__main__":
        print(fib(n))
main()