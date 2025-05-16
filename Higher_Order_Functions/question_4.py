def reduce(callback, iterable, starting):
    product = starting
    for number in iterable:
        product = callback(number, product)
    return product

# compute the sum of squares of a list of numbers
numbers = list(range(46))
# first calculate squares, then call reduce on the squares
sum_of_squares = reduce(lambda number, accum: number ** 2 + accum, numbers, 0)
print(sum_of_squares == sum([number ** 2 for number in numbers]))