from enum import IntEnum
from typing import Tuple,List

Nucleotide: IntEnum = IntEnum('Nucleotide', ('A', 'C', 'G', 'T'))

''' The use of IntEnum above rather than Enum is because it allows for 
comparative operators such as = < > etc for free.'''

''' Context for DNA - a Codon is a Tuple of three Nucleotides '''

