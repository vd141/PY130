'''
question 1
'''
# expression = (1 / n for n in range(1, 11))
# for number in expression:
#     print(number)

'''
question 2
'''
def gen_func(top):
    generator = (1 / n for n in range(1, top + 1))
    for number in generator:
        print(number)

# gen_func(10)

'''
question 3
'''
listostrings = list('qwerty')
capitalized = (word.capitalize() for word in listostrings)
# print(tuple(capitalized))

'''
question 4
'''
def gen_func(listofstrings):
    generator = (mini.capitalize() for mini in listofstrings)
    print(tuple(generator))

gen_func(listostrings)