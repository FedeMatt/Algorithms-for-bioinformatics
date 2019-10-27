def HammingDistance(pattern1,pattern2):
    return len([base for i,base in enumerate(pattern1) if base != pattern2[i]])

def DistanceBetweenPatternAndStrings(pattern,Dna):
    k = len(pattern)
    distance = 0
    for DNA in Dna:
        HDs = [HammingDistance(pattern, DNA[pos:pos+k]) for pos in range(len(DNA)-k+1)]
        distance += min(HDs)
    return distance
