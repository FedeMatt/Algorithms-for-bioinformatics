def All_aprox_occ(string, DNA, d):
    n = len(DNA)
    k = len(string)
    result = []
    for start_pos in range(n-k+1):
        kmer = DNA[start_pos:start_pos+k]
        hamming_d = sum(ch1 != ch2 for ch1, ch2 in zip(string, kmer))
        if hamming_d <= d:
            result.append(start_pos)
    for j in result:
        print(j, end = " ")
