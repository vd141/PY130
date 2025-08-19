'''
Write a program that takes a word and a list of possible anagrams and selects 
the correct sub-list that contains the anagrams of the word.

For example, given the word "listen" and a list of candidates like "enlists", 
"google", "inlets", and "banana", the program should return a list containing 
"inlets". Please read the test suite for the exact rules of anagrams.
'''

class Anagram():
    def __init__(self, word=''):
        self._base_word = word

    def match(self, words_list):
        # returns a sublist of valid anagrams from other
        # if there are no valid anagrams in other, return an empty list
        # identical words are not allowed
        return [word for word in words_list if self._is_anagram(word) and
                word.casefold() != self._base_word.casefold()]

    def _is_anagram(self, other):
        # a word is an anagram if it can be made from the exact same letters
        # of the base word
        # all letters are compared on a casefold() basis
        # store letters and count into a hashmap. compare hashmaps. if hashmaps
        # are equal, the other letter is a valid anagram
        return Anagram.hashmap_word(self._base_word) == Anagram.hashmap_word(other)

    @staticmethod
    def hashmap_word(word):
        word_hashmap = {}
        for letter in word:
            word_hashmap[letter.casefold()] = word_hashmap.get(letter.casefold(), 0) + 1
        return word_hashmap
