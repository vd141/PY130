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
        # find the len of the shorter strand
        # loop over both strands and add a difference to a variable called diff
        # count
        hamming_distance = 0
        loop_size = min(len(self._strand), len(other_strand))
        for i in range(loop_size):
            hamming_distance += 1 if self._strand[i] != other_strand[i] else 0
        return hamming_distance