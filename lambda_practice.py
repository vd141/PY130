'''
lambda function practice problems
'''
# lambda function that squares a number

squared = lambda num: num ** 2
listonums = [1, 2, 3, 4, 5]
def each(callback, iterable):
    return [callback(item) for item in iterable]
sq_results = each(squared, listonums)
print(sq_results)

# lambda that returns True if a number is even
# use it with filter() on the list []
numbers = [1, 2, 3, 4, 5, 6]
print(list(filter(lambda a: a % 2 == 0, numbers)))

# lambda that tests length of string
ret_len = lambda word: len(word)
print(ret_len('hello'))

# lambda that adds two numbers
add_two = lambda a, b: a + b
print(add_two(4, 9))

# sort by second letter
words = {'banana', 'apple', 'cherry', 'date', 'monk'}
print(sorted(words, key=lambda word: word[1]))

# convert to title case using map()
names = ['john', 'paul', 'george', 'ringo']
cap_names = map(lambda name: name.capitalize(), names)
print(list(cap_names))

# filter strings with more than 4 letters
animals = ['dog', 'elephant', 'cat', 'horse', 'ant']
print(list(filter(lambda word: len(word) > 4, animals)))

# sort list of tuples by second element
pairs = [(1, 2), (3, 1), (5, 0)]
# Should become [(5, 0), (3, 1), (1, 2)]
print(sorted(pairs, key=lambda pair: pair[1]))

# sum of squares. find the sum of squares from 1 to 10
print(sum(map(lambda a: a ** 2, range(1, 11))))

# create a list of lambda functions that each return their index cubed

functions = [lambda x=i: x ** 3 for i in range(5)]
print([f() for f in functions])  # [0, 1, 8, 27, 64]