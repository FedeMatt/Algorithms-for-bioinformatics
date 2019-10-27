def CountBreakpoints(sp):
    out = 0
    for j in range(len(sp)-1):
        if sp[j+1] - sp[j] != 1:
            out+=1
    return out
