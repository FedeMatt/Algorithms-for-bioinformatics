def find_occ_pat(DNA, m):
    n = len(DNA)
    d = {}
    k = len(m)
    result = []
    for start_pos in range(0, n-k+1):
        kmer = DNA[start_pos:start_pos+k]
        if kmer == m:
            result.append(start_pos)
    for j in result:
        print(j, end = " ")
