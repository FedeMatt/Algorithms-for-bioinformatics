def Generate_kmer_Composition_of_a_String(text, k):
    return sorted([text[start_pos:start_pos+k] for start_pos in range(0,len(text)-k+1)])
