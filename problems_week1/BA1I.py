from itertools import product
import pandas as pd
import multiprocessing as mp

def HammingDistance(pattern1,pattern2):
    return sum(ch1 != ch2 for ch1, ch2 in zip(pattern1, pattern2))

def CountApproxOccurrences(pattern,patterns,d):
    return sum(1 for pat in patterns if 
               HammingDistance(pattern, pat) <= d)
    
def AllSimilarPatterns(pattern, all_patterns,d):
    return pd.Series([pat for pat in 
                      all_patterns if 0<=HammingDistance(pattern,pat)<=d])

def MostFrequentPatterns(patterns_freq):
    max_frequence = patterns_freq.max()
    return list(patterns_freq[patterns_freq == max_frequence].index)
    
def FrequentWordsMis(genome,k,d):
    n = len(genome)
    
    "Generate all patterns"
    patterns = pd.Series([genome[pos:pos+k] for pos in range(n-k+1)])
    
    "Remove all duplicated patterns"
    patterns_no_duplicates = patterns.unique()
    
    "Generate all possible patterns of length k"
    all_patterns = pd.Series(["".join(base) for base
                              in product(list('ATCG'),repeat=k)])
    
    "Generate all similar patterns of the existing ones removing every eventual duplicate"
    pool = mp.Pool(mp.cpu_count())
    similar_p= pd.concat(pool.starmap(AllSimilarPatterns,[(pattern,all_patterns,d) 
                                        for pattern in patterns_no_duplicates]))
    pool.close()
    similar_p = similar_p.unique()
    
    "Compute the number of similar patterns for each pattern built so far"
    freq_words_mis = pd.Series([CountApproxOccurrences(pattern,patterns,d) 
                                for pattern in similar_p], index = similar_p)
    
    "Return the most frequent pattern with mismatches"
    return set(MostFrequentPatterns(freq_words_mis))
