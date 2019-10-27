import numpy as np

def FittingAlignmentProblem(v, w):

    out = np.zeros((len(w)+1, len(v)+1))
    for i in range(1, len(w)+1):
        for j in range(1, len(v)+1):
            horizon = out[i,j-1] - 1
            verv = out[i-1,j] - 1
            if w[i-1] == v[j-1]:
                outiag = out[i-1,j-1] + 1
            else:
                outiag = out[i-1,j-1] - 1

            out[i,j] = max(horizon, verv, outiag)
    #print(out)

    score = max(out[-1])

    res1 = []
    res2 = []
    i = len(out) - 1
    while True:
        if out[i,j] == out[i-1,j-1] + (1 if v[j-1] == w[i-1] else -1):
            res1 = [v[j-1]] + res1
            res2 = [w[i-1]] + res2
            i -= 1
            j -= 1
        else:
            max_el = max(out[i,j-1], out[i-1][j])
            if max_el == out[i,j-1]:
                res1 = [v[j-1]] + res1
                res2 = ["-"] + res2
                j -= 1
            elif max_el == out[i-1][j]:
                res1 = ["-"] + res1
                res2 = [w[i-1]] + res2
                i -= 1

        if i == 0 or j == 0:
            break

    print(score)
    print("".join(res1))
    print("".join(res2))
