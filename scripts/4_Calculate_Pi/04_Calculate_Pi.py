#!/usr/bin/env python3

''' 
Python implementation of the Liebniz formmula
for the calculation/approximation  of Pi
https://en.wikipedia.org/wiki/Leibniz_formula_for_%CF%80
'''

'''
Might I suggest bearing this formula in mind and then
experimenting with the number of iterations. You'll see
it converge on pi and then realise how freaky this whole
thing is and what a strange number it is and then you'll
start to question everything and maybe go a little mad 
and who says you can't talk to a cucumber?

That's what they want you to think.
'''

import sys

def calculate_pi(n_terms: int) -> float:
    numerator: float = 4.0
    denominator: float = 1.0
    operation: float = 1.0
    pi: float = 0.0

    for lol in range(n_terms):
        pi += operation * (numerator / denominator)
        denominator += 2.0
        operation *= -1.0
    return pi

if __name__ == "__main__":
    places = int(sys.argv[1])
    print(calculate_pi(places))