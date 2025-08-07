'''
Q1: generator expression that generates the reciprocals from 1 to 10. a reciprocal
of number n is 1 / n. use a for loop to print each value
'''
recips = (1 / item for item in range(1,11))
for value in recips:
    print(value)

'''
Q2
'''
def generate_recips(up_to_me):
    for value in range(1, up_to_me + 1):
        yield 1 / value

recips = generate_recips(10)
for value in recips:
    print(value)

'''
Q3

use a generator expression to capitalize every string in a list of strings
use a single print invocation to print all capitalized strings as a tuple
'''
listostrigs = ['asdf', 'dd', 'afdsads', 'i', 'boondogle']
capitalized = (word.capitalize() for word in listostrigs)
print(tuple(capitalized))

'''
Q4

same as above, but use a generator function
'''
def capitalizer(listostrings):
    for word in listostrings:
        yield word.capitalize()

capitalized = capitalizer(listostrigs)
print(tuple(capitalized))

'''
Q5

use a generator to capitalize and select only the words in a list that are at 
least len 5 then print the generator words in a set
'''
strings = ['four', 'score', 'and', 'seven', 'years', 'ago']

at_least_five = (word.capitalize() for word in strings if len(word) >= 5)
print(set(at_least_five))

'''
Q6

create a generator function that generates the capitalized version of every string
in a list of strings whose length is less than 5. use a single print invocation to 
print each of those words in a set
'''

def less_than_five_cap(strings):
    for word in strings:
        if len(word) < 5:
            yield word.capitalize()

print(set(less_than_five_cap(strings)))