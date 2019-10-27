def PrefixTrieMatching(text, trie):
    i = 0 
    symbol = text[i]
    v = 0
    out = []
    while i!= len(text):
        if v not in trie:
            return "".join(out)
        elif symbol in trie[v]:
            try:
                i+=1
                out.append(symbol)
                v = trie[v][symbol]

                symbol = text[i]  
            except:
                continue
        else:
            return "no matches found"           
        
def TrieMatching(text, trie):
    for i in range(len(text)-1):
        aa = PrefixTrieMatching(text, trie)
        text = text[1:]  
        if aa != "no matches found":
            print(i, end=" ")