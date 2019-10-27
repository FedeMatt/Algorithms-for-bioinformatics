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

score = get_score_matrix("PAM250.txt")

def high_score_align(str1, str2):
    sigma = 5
    cols_num = len(str1)
    rows_num = len(str2)
    dist_matr = np.zeros((rows_num + 1, cols_num + 1))
    for i in range(cols_num):
        dist_matr[0,i+1] = dist_matr[0,i] - sigma

    for i in range(rows_num):
        dist_matr[i+1,0] = dist_matr[i,0] - sigma

    for i in range(rows_num):
        for j in range(cols_num):
            dist_matr[i+1,j+1] = max(0,
                        dist_matr[i,j+1] - sigma,
                        dist_matr[i+1,j] - sigma,
                        dist_matr[i,j] + score(str2[i], str1[j]))




    max_score = 0
    for k in range(rows_num + 1):
        for t in range(cols_num + 1):
            if max_score < dist_matr[k,t]:
                max_score = dist_matr[k,t]
                i = k - 1
                j = t - 1

    answ1 = []
    answ2 = []

    while i != -1 or j != -1:
        max_el = dist_matr[i+1,j+1] - score(str2[i], str1[j])
        if max_el == dist_matr[i,j]:
            answ1 = [str1[j]] + answ1
            answ2 = [str2[i]] + answ2
            i -= 1
            j -= 1
        else:
            max_el = max(dist_matr[i+1,j], dist_matr[i,j+1])
            if max_el == dist_matr[i+1,j]:
                answ1 = [str1[j]] + answ1
                answ2 = ["-"] + answ2
                j -= 1
            else:
                answ1 = ["-"] + answ1
                answ2 = [str2[i]] + answ2
                i -= 1

        if max_el == 0:
            break

    print(int(max_score))
    print("".join(answ1))
    print("".join(answ2))
