def ReverseComplement(pattern):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return "".join(complement.get(base) for base in reversed(pattern))
