import numpy as np
from operator import itemgetter
import random

def RandomMotifsMatrix(Dna):
    # Dna is a list of strings
    Motifs = []
    for DNA in Dna:
        random_index = np.random.randint(len(DNA)-k+1)
        Motifs.append(list(DNA[random_index:random_index+k]))
    return np.array(Motifs)

def PseudocountMatrix(Motifs):
    # Motifs is a numpy matrix
    row = {'A':0, 'C':1, 'G':2, 'T':3}
    Pseudocount = np.ones((4,Motifs.shape[1]),dtype=int)
    for j in range(Motifs.shape[1]):
        for i in range(Motifs.shape[0]):
            Pseudocount[row[Motifs[i,j]],j]+=1
    return Pseudocount

def PseudoProfileMatrix(Motifs):
    Pseudocount = PseudocountMatrix(Motifs)
    t = Motifs.shape[0]
    return Pseudocount/(t+4)

def ProfileProbability(Profile,kmer):
    prob = 1
    row = {'A':0, 'C':1, 'G':2, 'T':3}
    for i,base in enumerate(kmer):
        prob*=Profile[row[base],i]
    return prob

def Score(Count):
    return sum(np.sum(Count[:,j])-np.max(Count[:,j]) for j in range(Count.shape[1]))


def RandomizedMotifSearch(Dna, k, t):
    # Dna is a list of strings

    # Create the BestMotifs matrix formed by first k-mer in each string from Dna
    Motifs = RandomMotifsMatrix(Dna)
    BestMotifs = Motifs

    for i in range(100):
        if i>0:
            Motifs = RandomMotifsMatrix(Dna)
            while True:
                Profile = PseudoProfileMatrix(Motifs)
                new_Motifs = []
                for DNA in Dna:
                    probabilities = {}
                    for pos in range(len(DNA)-k+1):
                        kmer = DNA[pos:pos+k]
                        if kmer not in probabilities:
                            probabilities[kmer] = ProfileProbability(Profile,kmer)
                    max_prob = max(probabilities.values())
                    for kmer in probabilities:
                        if probabilities[kmer] == max_prob:
                            Motif_i = kmer
                            new_Motifs.append(list(Motif_i))
                            break
                Motifs = np.array(new_Motifs)
                if Score(PseudocountMatrix(Motifs)) < Score(PseudocountMatrix(BestMotifs)):
                    BestMotifs = Motifs
                else:
                    break

    BestMotifs = [''.join(row) for row in BestMotifs]
    return BestMotifs
