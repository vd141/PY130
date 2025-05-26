from functools import reduce

numbers = list(range(1, 6))
print(reduce(lambda a, b: a * b, numbers))