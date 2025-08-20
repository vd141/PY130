# Write a program that, given a word, computes the Scrabble score for that word.
# A, E, I, O, U, L, N, R, S, T	  1
# D, G	                          2
# B, C, M, P	                  3
# F, H, V, W, Y	                  4
# K	                              5
# J, X	                          8
# Q, Z	                          10

from functools import reduce

class Scrabble:
    # scrabble has two public methods: score() and calculate_score()
    # score calculates the score of the word that Scrabble was initialized with
    # calculate_score() calculates the score of any word given as an argument

    LETTER_POINTS = {
        'a': 1,
        'b': 3,
        'c': 3,
        'd': 2,
        'e': 1,
        'f': 4,
        'g': 2,
        'h': 4,
        'i': 1,
        'j': 8,
        'k': 5,
        'l': 1,
        'm': 3,
        'n': 1,
        'o': 1,
        'p': 3,
        'q': 10,
        'r': 1,
        's': 1,
        't': 1,
        'u': 1,
        'v': 4,
        'w': 4,
        'x': 8,
        'y': 4,
        'z': 10,
    }

    def __init__(self, word):
        self._word = word

    @staticmethod
    def calculate_score(word):
        if not isinstance(word, str):
            return 0
        word_score = 0
        for letter in word.casefold():
            word_score += Scrabble.LETTER_POINTS.get(letter, 0)
        return word_score

    def score(self):
        return Scrabble.calculate_score(self._word)