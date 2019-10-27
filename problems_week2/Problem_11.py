import numpy as np

def BuildProfileMatrixByStrings(Profile):
    Profile = Profile.split('\n')
    Profile = [profile.split(' ') for profile in Profile]
    Profile = np.array(Profile, dtype=float)
    return Profile

def KmerProfileProbability(kmer,Profile):
    # Profile is a numpy matrix 4xlen(kmer)
    row = {'A':0, 'C':1, 'G':2, 'T':3}
    prob = 1
    for col,base in enumerate(kmer):
        prob *= Profile[row[base],col]
    return prob

def ProfileMostProbableKmer(text,k,Profile):
    # Profile is a multirow string
    Profile = BuildProfileMatrixByStrings(Profile)

    kmers = list(set([text[pos:pos+k] for pos in range(len(text)-k+1)]))
    kmer_probs = {}
    for kmer in kmers:
        kmer_probs[kmer] = KmerProfileProbability(kmer,Profile)
    max_prob = max(kmer_probs.values())
    for kmer in kmer_probs:
        if kmer_probs[kmer] == max_prob:
            return kmer   
