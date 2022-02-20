#!/usr/bin/env python3

''' Note the use of the underscore for the compress
method in the CompressedGene class. Python has no real
concept of private methods, but the underscore is used
to indicate that it should not be relied upon by actors
outside of the class

Python will "name mangle" any methods or variable in a
class that has double underscore using a salt to make it
not easily discoverable outside.'''

from genericpath import getsize

class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1 # start with sentinel
        for nucleotide in gene.upper():
            self.bit_string <<= 2 # shift left two bits
            
            if nucleotide == "A": # change the last two bits to 00
                self.bit_string |= 0b00
            elif nucleotide == "C": # change the last two bits to 01
                self.bit_string |= 0b01
            elif nucleotide == "G": # change the last two bits to 10
                self.bit_string |= 0b10
            elif nucleotide == "T": # change the last two bits to 11
                self.bit_string |= 0b11
            else:
                raise ValueError("Invalid nucleotide: {}".format(nucleotide))

    def decompress(self) -> str:
        gene: str = ""
        for i in range(0, self.bit_string.bit_length() - 1, 2): # -1 to exclude sentinel
            bits: int = self.bit_string >> i & 0b11 # just get two relevant bits
            if bits == 0b00: # A
                gene += "A"
            elif bits == 0b01: # C
                gene += "C"
            elif bits == 0b10: # G
                gene += "G"
            elif bits == 0b11: # T
                gene += "T"
            else:
                raise ValueError("Invalid bits: {}".format(bits))
        return gene[::-1] # reverses the string by slicing backwards

    def __str__(self) -> str: # string representation for pretty print
        return self.decompress()

if __name__ == "__main__":
    from sys import getsizeof
    original: str = "TAGGGATTAACCGCAGTACGCATCGATCGATCGACTAGTCGATCACTATCGGTCGATACGATGTCAGTGTGAGCGCGATCGCTAGCGCTACGGCTAGCGGCTGC" * 10
    original_size = int(getsizeof(original))
    print("\nOriginal is size {} bytes\n".format(getsizeof(original)))

    compressed: CompressedGene = CompressedGene(original) # Compress it
    compressed_size = int(getsizeof(compressed.bit_string))
    print("Compressed is size {} bytes\n".format(getsizeof(compressed.bit_string)))

    ratio = round(((compressed_size / original_size) * 100),2)
    print("Compressed file is {} percent of the original file\n".format(ratio))

    comparison: str = str((original == compressed.decompress()))
    print("Original and decompressed are the same: {} ".format(comparison))
