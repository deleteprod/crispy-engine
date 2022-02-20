#!/usr/bin/env python3

''' In this example we will recreate the equivalent of using a
one time pad for encrypting and decrypting a message in Python

Encryption:

Original Data -------\  /-------Key 1 (Dummy Data)
                      XOR
Dummy Data    -------/  \-------Key 2 (Product) 

Decryption:

Key 1 (Dummy Data) ---\ 
                       XOR ---> Original Data
Key 2 (Product)    ---/
'''

from secrets import token_bytes
from typing import Tuple

def random_key(length: int) -> int:
    # generate random bytes
    tb: bytes = token_bytes(length)
    # convert the bytes to a bit string and return it
    return int.from_bytes(tb, "big")

def encrypt(original: str) -> Tuple[int, int]:
    