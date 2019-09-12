def Pos_min_skew(DNA):
    result = [0]
    DNA = list(DNA)
    for i, occ in enumerate(DNA):
        if occ == "C":
            result.append(result[i] - 1)
        elif occ == "G":
            result.append(result[i] + 1)
        else:
            result.append(result[i])
    print("starting the hard task...")
    min_ = min(result)
    output = [j for j,count in enumerate(result) if count==min_]
    for r in output:
        print(r, end=" ")
