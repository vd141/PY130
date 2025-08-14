# calculate product of all numbers in a list using the reduce function

from functools import reduce
og_list = [1, 2, 3, 4]
# reduce takes a lambda, iterable, accumulator

reduced = reduce(lambda a, accum: a * accum, og_list, 1)
print(reduced) # 24