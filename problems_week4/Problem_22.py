def lcs(s1, s2):
    n = len(s1)
    m = len(s2)
    table = dict()

    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                table[i, j] = 0
            elif s1[i-1] == s2[j-1]:
                table[i, j] = table[i-1, j-1] + 1
            else:
                table[i, j] = mas1(table[i-1, j], table[i, j-1])

    def recon(i, j):
        if i == 0 or j == 0:
            return []
        elif s1[i-1] == s2[j-1]:
            return recon(i-1, j-1) + [s1[i-1]]
        elif table[i-1, j] > table[i, j-1]:
            return recon(i-1, j)
        else:
            return recon(i, j-1)

    return "".join(recon(n, m))
