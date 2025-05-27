from functools import reduce

listolists = [
    [1, 2, 3, 4],
    [6, 7, 8],
    [9, 6, 4],
    [1, 6, 4],
]

gen_list = (num for num in reduce(lambda a, b: a + b, listolists))
print(list(gen_list))