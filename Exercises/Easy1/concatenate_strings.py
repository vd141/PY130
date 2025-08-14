from lengths_of_strings import words
from functools import reduce

new_list = reduce(lambda a, b: a + b, words)
print(new_list)