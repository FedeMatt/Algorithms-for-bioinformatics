import numpy as np
from operator import itemgetter

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


def PseudoGreedyMotifSearch(Dna, k, t):
    # Dna is a list of strings

    # Create the BestMotifs matrix formed by first k-mer in each string from Dna
    BestMotifs = np.array([list(DNA[:k]) for DNA in Dna])

    for pos in range(len(Dna[0])-k+1):

        # At the beginning, the Motifs matrix is formed just by a k-mer in the first string from Dna
        Motifs = np.array(list(Dna[0][pos:pos+k]))[np.newaxis,:]

        for i in range(1,t):
            # Build the Profile matrix of the Motifs matrix
            Profile = PseudoProfileMatrix(Motifs)

            # Find the Profile-most probable kmer in the i-th string in Dna
            probabilities = {}
            for ipos in range(len(Dna[i])-k+1):
                #print(range(len(Dna[i])-k+1))
                #print(Dna[i][len(Dna[i])-k:len(Dna[i])])
                kmer = Dna[i][ipos:ipos+k]
                if kmer not in probabilities:
                    probabilities[kmer] = ProfileProbability(Profile,kmer)
            max_prob = max(probabilities.values())
            for kmer in probabilities:
                if probabilities[kmer] == max_prob:
                    Motif_i = kmer
                    break

            # Concatenate such kmer to the Motifs matrix
            Motifs = np.concatenate((Motifs,np.array(list(Motif_i))[np.newaxis,:]),axis=0)

        # Set as BestMotifs matrix, the one between Motifs and old BestMotifs that has the lowest score
        if Score(PseudocountMatrix(Motifs)) < Score(PseudocountMatrix(BestMotifs)):
            BestMotifs = Motifs
    BestMotifs = [''.join(row) for row in BestMotifs]

    return BestMotifs
