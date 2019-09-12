from itertools import product
import pandas as pd
import multiprocessing as mp

def HammingDistance(pattern1,pattern2):
    return sum(ch1 != ch2 for ch1, ch2 in zip(pattern1, pattern2))

def CountApproxOccurrences(pattern,patterns,d):
    return sum(1 for pat in patterns if 
               HammingDistance(pattern, pat) <= d)

def AllSimilarPatterns(pattern, all_patterns,d):
    return pd.Series([pat for pat in all_patterns if 0<=HammingDistance(pattern,pat)<=d])

def MostFrequentPatterns(patterns_freq):
    max_frequence = patterns_freq.max()
    return list(patterns_freq[patterns_freq == max_frequence].index)

def ReverseComplement(pattern):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} 
    return "".join(complement.get(base) for base in reversed(pattern))
    
def FrequentWordsMisRc(genome,k,d):
    n = len(genome)
    
    "Generate all patterns"
    patterns = pd.Series([genome[pos:pos+k] for pos in range(n-k+1)])
        
    "Remove all duplicated patterns"
    patterns_no_duplicates = patterns.unique()
        
    "Generate all possible patterns of length k"
    all_patterns = pd.Series(["".join(base) for
                                     base in product(list('ATCG'), repeat=k)])
    
    "Generate all similar patterns of the existing ones removing every eventual duplicate"
    pool = mp.Pool(mp.cpu_count())
    similar_patterns = pd.concat(pool.starmap(AllSimilarPatterns,[(pattern,all_patterns,d) 
                                                for pattern in patterns_no_duplicates]))
    pool.close()
    similar_patterns = pd.Series(similar_patterns.unique())    
    
    """ Generate a series where each index is one pattern (of the one generated so far) 
     and its value is the revers complement pattern 
     We have to do this procedure symmetrically."""
    
    rc_similar_p = pd.Series([ReverseComplement(pattern) for pattern in similar_patterns])

    rc_similar_p_index = pd.concat([similar_patterns,rc_similar_p], 
                                          ignore_index=True)
    rc_similar_p_index = rc_similar_p_index.values

    rc_similar_p_values = pd.concat([rc_similar_p,similar_patterns], 
                                           ignore_index=True)
    rc_similar_p_values = rc_similar_p_values.values

    rc_similar_p_sym= pd.Series(rc_similar_p_values,
                                       index = rc_similar_p_index)

    """For each tuple, compute the sum of the occurrences of 
    the pattern and its reverse complement in the genome"""
    freq_p = pd.Series([CountApproxOccurrences(pat,patterns,d)+
                           CountApproxOccurrences(rc_pat,patterns,d) for
                     pat, rc_pat in rc_similar_p_sym.items()], 
                          index = rc_similar_p_index)

    return set(MostFrequentPatterns(freq_p))
