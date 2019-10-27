import numpy as np

class get_score_matrix(object):
    """Reads a scoring matrix from a given file and returns a scoring function.
    Usage:
    score = get_score_matrix("blosum62.txt")
    score("A", "D") == -2"""

    def __init__(self, filename):
        scorefile = open(filename, "r")
        alphabet = scorefile.readline().split()
        self.scorematrix = []
        for line in scorefile:
                self.scorematrix.append(list(map(int,line.split()[1:])))
        scorefile.close()

        # Dictionary from alphabet to integers
        self.toint = dict(zip(alphabet, range(len(alphabet))))

    def __call__(self, a, b):
        return self.scorematrix[self.toint[a]][self.toint[b]]

score = get_score_matrix("blosum62.txt")

def DefineMatrix(v, w, sigma):
    """Compute the Edit Matrix starting from two strings v and w"""
    S = np.array([[0 for j in range(len(w)+1)] for i in range(len(v)+1)])
    for i in range(1, len(v)+1):
        S[i,0] = -i*sigma
        for j in range(1, len(w)+1):
            S[0,j] = -j*sigma
    return S



def GBM(v, w, sigma):
    """Compute the score matrix starting from two strings v, w and sigma penalization
        for indel"""
    matrix = DefineMatrix(v, w, sigma)
    # Fill in the Score and Backtrack matrices.
    for i in range(1, len(v)+1):
        for j in range(1, len(w)+1):
            matrix[i,j] = np.max([matrix[i-1,j] - sigma,
                                  matrix[i,j-1] - sigma,
                                  matrix[i-1,j-1] + score(v[i-1], w[j-1])])
    return matrix.T


def TraceBack():
    dist_matr = GBM(v, w, sigma)
    max_score = dist_matr[len(w),len(v)]
    answ1 = []
    answ2 = []
    i = len(w) - 1
    j = len(v) - 1
    while i != -1 or j != -1:
        max_el = dist_matr[i+1,j+1] - score(v[j], w[i])
        if max_el == dist_matr[i,j]:
            answ1 = [v[j]] + answ1
            answ2 = [w[i]] + answ2
            i -= 1
            j -= 1
        else:
            max_el = max(dist_matr[i+1,j], dist_matr[i,j+1])
            if max_el == dist_matr[i+1,j]:
                answ1 = [v[j]] + answ1
                answ2 = ["-"] + answ2
                j -= 1
            else:
                answ1 = ["-"] + answ1
                answ2 = [w[i]] + answ2
                i -= 1

    print(int(max_score))
    print("".join(answ1))
    print("".join(answ2))
