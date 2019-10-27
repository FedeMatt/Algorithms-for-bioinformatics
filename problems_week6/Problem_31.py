def SuffixArray(Text):
    l = [(Text[j:],j)  for j in range(len(Text))[::-1]]
    new_l = [index[1] for index in sorted(l)]
    for number in new_l:
        if number == new_l[-1]:
            print(number, end = "")
        else:    
            print(number, end=", ")