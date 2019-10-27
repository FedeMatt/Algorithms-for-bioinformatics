def BWT(Text):
    l = [Text[j:] + Text[:j] for j in range(len(Text))[::-1]]
    print("".join([word[-1] for word in sorted(l)]))
