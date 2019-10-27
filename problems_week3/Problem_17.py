def deBruijnGraph(text, k):
    c = k-1
    result = dict()
    for start_pos in range(len(text)-c+1):
        kmer = text[start_pos:start_pos+c]
        result[kmer] = []

    for kmer_1 in result:
        for kmer_2 in result:
            if kmer_1[1:] == kmer_2[:-1]:
                result[kmer_1].append(kmer_2)
    l = 0
    for kmer in result:
        if result[kmer] == []:
            l = kmer
    del result[l]
    return sorted(result.items())

k  = 4
text = "AAGATTCTCTAC"
output = deBruijnGraph(text, k)
for j, i in output:
    print(j, "->", ",".join(i))

output = deBruijnGraph(text, k)
for j, i in output:
    jj = ",".join(i)
    print(j, "->", jj)
