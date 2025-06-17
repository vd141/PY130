'''
calculate the hamming distance between two DNA strands

the hamming distanace is only defined for sequences of equal length. 
if you have two sequences of unequal length, you should compute the hamming
distance over the shorter length

DNA class takes a string when initialized

calls a method called hamming_distance which takes another string and calculates
the hamming distance
'''

class DNA:
    def __init__(self, strand):
        self._strand = strand
    
    def hamming_distance(self, other_strand):
        hamming= 0
        shorter = (self._strand 
                   if len(self._strand) <= len(other_strand )
                   else other_strand)
        longer = (self._strand 
                   if len(self._strand) > len(other_strand )
                   else other_strand)
        for index, nucleotide in enumerate(shorter):
            if nucleotide != longer[index]:
                hamming += 1
        return hamming