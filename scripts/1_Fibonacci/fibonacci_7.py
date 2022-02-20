#!/usr/bin/env python3

# Usage <scriptname.py> <integer>

'''
Improved version, this time let's look at the use of
a generator in Python'''

import sys
from typing import Generator

# Takes passed argument
n = int(sys.argv[1])

def fib(n: int) -> Generator[int, None, None]:
    yield 0 # special case
    if n > 0: yield 1 # special case
    last: int = 0 # set initial val for fib(0)
    next: int = 1 # set initial val for fib(1)
    for lol in range (1, n):
        last, next = next, last + next
        yield next # main generation step


def main():
    if __name__ == "__main__":
        for i in fib(n):
            print(i)
        #print(fib(n))
main()