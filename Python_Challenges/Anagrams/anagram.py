'''
Write a program that takes a word and a list of possible anagrams and selects 
the correct sub-list that contains the anagrams of the word.

For example, given the word "listen" and a list of candidates like "enlists", 
"google", "inlets", and "banana", the program should return a list containing 
"inlets". Please read the test suite for the exact rules of anagrams.
'''

'''
an anagram contains the same number of letters as the original. it cannot be
equal to the original

one way to compare two strings is to sort both alphabetically and casefold 
(case doesn't matter). then compare the sorted strings
'''

class Anagram:
    def __init__(self, base_word):
        self._base_word = base_word
    
    def match(self, list_of_anagrams):
        result = []
        for word in list_of_anagrams:
            if ((sorted(word.casefold()) == sorted(self._base_word.casefold())) 
                and (word.casefold() != self._base_word.casefold())):
                result.append(word)
        return result


