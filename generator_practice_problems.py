'''
question 1
'''
generator = (1 / n for n in range(1, 11))

# for elem in generator:
#     print(elem)

'''
question 2
'''
# def genfunc(n):
#     return (1 / number for number in range(1, n + 1))

# for n in genfunc(5):
#     print(n)

#  alternate solution
def genfunc(n):
    for number in range(1, n + 1):
        yield 1 / number

# for n in genfunc(5):
#     print(n)

'''
question 3
'''
listostrings = list('abdfwasdfc')
# print(tuple((string.capitalize() for string in listostrings)))

'''
question 4
'''
def capitalize_strings(listostrings):
    for string in listostrings:
        yield string.capitalize()

# print(tuple(capitalize_strings(listostrings)))

'''
question 5
'''
listostrings = ['four', 'five', 'seven', 'nine', 'twenty-four']
generated = (string.capitalize()
             for string in listostrings
             if len(string) >= 5)
print(set(generated))

'''
question 6
'''
generated = (string.capitalize()
             for string in listostrings
             if len(string) < 5)
print(set(generated))