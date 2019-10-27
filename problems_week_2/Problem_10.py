from itertools import product

def HammingDistance(pattern1,pattern2):
    return len([base for i,base in enumerate(pattern1) if base != pattern2[i]])

def DistanceBetweenPatternAndStrings(pattern,Dna):
    # Dna is a list of strings
    k = len(pattern)
    distance = 0
    for DNA in Dna:
        HDs = [HammingDistance(pattern, DNA[pos:pos+k]) for pos in range(len(DNA)-k+1)]
        distance += min(HDs)
    return distance

def AllKmers(k):
    return ["".join(base) for base in product(list('ATCG'),repeat=k)]

def AllSimilarPatterns(pattern, all_kmers,d):
    return [pat for pat in all_patterns if 0<=HammingDistance(pattern,pat)<=d]

def FindMedianString(k, Dna):
    # Dna is a list of strings
    patterns = {}
    all_kmers = AllKmers(k)
    for kmer in all_kmers:
        if kmer not in patterns:
            patterns[kmer] = DistanceBetweenPatternAndStrings(kmer,Dna)
    min_distance = min(patterns.values())
    for pat in patterns:
        if patterns[pat] == min_distance:
            return pat
