def find_most_fw(DNA, k):
    n = len(DNA)
    k = int(k)
    d = {}
    for start_pos in range(0, n-k+1):
        kmer = DNA[start_pos:start_pos+k]
        if kmer in d:
            d[kmer] +=1
        else:
            d[kmer] = 1

    max_count = 0
    result = []
    for kmer in d:
        if d[kmer] > max_count:
            max_count = d[kmer]
    for kmer in d:
        if d[kmer] == max_count:
            result.append(kmer)

    return (" ".join(result))
