def find_clumps(genome,k,L,t):
    clumps = []
    n = len(genome)
    for i in range(n-L+1):
        kmers = {}
        for pos in range(i,i+L):
            if pos+k-1<i+L:
                km = genome[pos:pos+k]
                if km not in clumps:
                    kmers.setdefault(km,[]).append(pos)
        clumps.extend([km for km in kmers if len(kmers[km]) >= t])

    for j in set(clumps):
        print(j, end=" ")
