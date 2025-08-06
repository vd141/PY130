'''
def for_each(callback, iterable):
    for item in iterable:
        callback(item)

for_each(lambda number: print(number**2), [1, 2, 3, 4, 5])

pets = ('cat', 'dog', 'fish', 'bearded dragon')
for_each(lambda string: print(string.title()), pets)
'''

'''
def times(callback, count):
    for index in range(count):
        callback(index)

times(lambda number: print(number**2), 5)

pets = ('cat', 'dog', 'fish', 'bearded dragon')
new_pets = []
times(lambda index: new_pets.append(pets[index].title()),
      len(pets))

print(new_pets)
'''

'''
# first pass: no comprehensions
def select(callback, iterable):
    # returns a list of all the elements that result in a truthy value when passed into the callback fxn
    new_list = []
    for element in iterable:
        if callback(element):
            new_list.append(element)
    return new_list
'''

# # second pass: comprehensions
# def select(callback, iterable):
#     return [element for element in iterable if callback(element)]


# numbers = [1, 2, 3, 4, 5]
# colors = {'red', 'orange', 'yellow', 'green',
#           'blue', 'indigo', 'violet'}

# odd_numbers = select(lambda number: number % 2 != 0, numbers)
# print(odd_numbers)            # [1, 3, 5]

# large_numbers = select(lambda number: number >= 10, numbers)
# print(large_numbers)          # []

# small_numbers = select(lambda number: number < 10, numbers)
# print(small_numbers)          # [1, 2, 3, 4, 5]

# short_color_names = select(lambda color: len(color) <= 5, colors)
# print(short_color_names)      # ['blue', 'red', 'green']
# # The order of the colors may vary, but should include the
# # indicated colors.

# def reject(callback, iterable):
#     return [element for element in iterable if not callback(element)]

# numbers = [1, 2, 3, 4, 5]
# colors = {'red', 'orange', 'yellow', 'green',
#           'blue', 'indigo', 'violet'}

# even_numbers = reject(lambda number: number % 2 != 0, numbers)
# print(even_numbers)            # [2, 4]

# small_numbers = reject(lambda number: number >= 10, numbers)
# print(small_numbers)          # [1, 2, 3, 4, 5]

# large_numbers = reject(lambda number: number < 10, numbers)
# print(large_numbers)          # []

# long_color_names = reject(lambda color: len(color) <= 5, colors)
# print(long_color_names)
# # ['yellow', 'violet', 'orange', 'indigo']
# # The order of the colors may vary, but should include the
# # indicated colors.

def reduce(callback, iterable, starting_val):
    # for every element in iterable, call the callback on that element
    # the collector gets the starting val and is updated every loop

    accum = starting_val
    for element in iterable:
        accum = callback(element, accum)
    return accum

numbers = (1, 2, 4, 8, 16)
total = lambda number, accum: accum + number
print(reduce(total, numbers, 0))        # 31

numbers = [10, 3, 5]
product = lambda number, accum: accum * number
print(reduce(product, numbers, 2))      # 300

colors = ['red', 'orange', 'yellow', 'green',
          'blue', 'indigo', 'violet']
rainbow = lambda color, accum: accum + color[0].upper()
print(reduce(rainbow, colors, ''))      # ROYGBIV

# Use the reduce function shown in the answer to the previous question to compute the sum of the squares in a list of numbers.

sum_sq = lambda item, accum: item ** 2 + accum
print(reduce(sum_sq, numbers, 0))