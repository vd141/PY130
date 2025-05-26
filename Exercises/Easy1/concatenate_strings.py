from lengths_of_strings import words
from functools import reduce

print((''.join(reduce(lambda a, b: a + b, words))))