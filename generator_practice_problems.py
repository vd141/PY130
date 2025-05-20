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
# def gen_func(listofstrings):
#     generator = (mini.capitalize() for mini in listofstrings)
#     print(tuple(generator))

# gen_func(listostrings)

def capped_strings(listostrings):
    for word in listostrings:
        yield word.capitalize()

# print(tuple(capped_strings(listostrings)))

'''
question 5
'''
def capped_strings_over_len5(listicle):
    for word in listicle:
        if len(word) >= 5:
            yield word.capitalize()

strings = ['four', 'score', 'and', 'seven', 'years', 'ago']
# print(set(capped_strings_over_len5(strings)))

'''
question 6
'''
def capped_strings_under_len5(listicle):
    for word in listicle:
        if len(word) < 5:
            yield word.capitalize()

print(set(capped_strings_under_len5(strings)))