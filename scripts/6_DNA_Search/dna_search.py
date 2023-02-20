from enum import IntEnum
from typing import Tuple,List

Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))

''' The use of IntEnum above rather than Enum is because it allows for 
comparative operators such as = < > etc for free.'''

''' Context for DNA - a Codon is a Tuple of three Nucleotides '''

Codon = Tuple[Nucleotide, Nucleotide, Nucleotide] # Type alias for Codon
Gene = List(Codon) # Type alias for genes

gene_str: str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"

def string_to_gene(s: str):
    gene: Gene = []
    for i in range(0, len(s), 3):
        if (i + 2) >= len(s): # Don't run off the end
            return gene
        codon: Codon = (Nucleotide[s[i]], Nucleotide[s[i+1]], Nucleotide[s[i+2]])
        gene.append(codon)
        return gene