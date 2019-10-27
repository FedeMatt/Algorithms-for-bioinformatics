from operator import itemgetter
def TrieConstruction(patterns):
    patterns = patterns.split("\n")
    Trie = {0:{}}
    for pattern in patterns:
        current_node = 0
        for i in range(len(pattern)):
            if pattern[i] in Trie[current_node].keys():
                current_node = Trie[current_node][pattern[i]] 
            else:
                new_node = len(Trie.keys())
                Trie[new_node] = {}
                Trie[current_node][pattern[i]] = new_node
                current_node = new_node
    l = len(Trie.keys())
    for i in range(l):
        if len(Trie[i])==0:
            del Trie[i]
    return Trie

t = TrieConstruction(patterns)
l = [(key, t[key][key_2], key_2) for key in t for key_2 in t[key]]
l = sorted(l, key=itemgetter(1))
for n1,n2,label in l:
    print(f"{n1}->{n2}:{label}")
