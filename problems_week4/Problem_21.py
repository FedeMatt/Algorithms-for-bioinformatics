import numpy as np

def EditMatrix(s1, s2):
    """Compute the Edit Matrix starting from two strings s1 and s2"""
    n1 = len(s1)
    n2 = len(s2)
    matrix = np.zeros((n1+1, n2), dtype=int)
    matrix = np.concatenate((np.arange(n1+1).T[:,np.newaxis], matrix), axis=1)
    matrix[0,:] = np.arange(n2+1)
    return matrix

def EditDistance(s1, s2):
    """Compute the Edit Distance starting from two strings s1 and s2"""
    matrix = EditMatrix(s1, s2)
    for i in range(len(s1)):
        for j in range(len(s2)):
            matrix[i+1,j+1] = min(matrix[i, j] + (0 if s1[i] == s2[j] else 1),
                                  matrix[i+1, j] + 1,
                                  matrix[i, j+1] +1)
    return matrix[len(s1), len(s2)] 
