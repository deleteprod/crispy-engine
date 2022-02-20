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
    original_bytes: bytes = original.encode()

    # Dummy text (OTP) of length equal to that being encrypted
    dummy: int = random_key(len(original_bytes))
    original_key: int = int.from_bytes(original_bytes, "big")
    encrypted: int = original_key ^ dummy # XOR the things
    return dummy, encrypted

def decrypt(key1: int, key2: int) -> str:
    decrypted: int = key1 ^ key2 # XOR the encryption away
    temp: bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")
    ''' It was necessary to add 7 to thge length of the decrypted data
    before using integer division (sometimes known as floor division) to avoid
    an off by one error.'''
    return temp.decode()

if __name__ == "__main__":
    # Pass in message, get key1 (dummy) and key2 (encrypted) text as return
    key1,key2 = encrypt("That")

    # Same in reverse, pass both into the decrypt function and get plaintext
    result: str = decrypt(key1, key2)
    print(result)