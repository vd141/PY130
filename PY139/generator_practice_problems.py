# q1
gen = (1 / n for n in range(1, 11))

# for element in gen:
#     print(element)

# q2
def generator(limit):
    for i in range(1, limit + 1):
        yield 1 / i

for i in generator(10):
    print(i)

# q3
a = tuple((b.capitalize() for b in ['abe', 'bondoc']))
print(a)

# q4
def capitalizer(liststrings):
    for word in liststrings:
        yield word.capitalize()

print(tuple(capitalizer(['abe', 'bondoc'])))

# q5
print(set((word.capitalize() for word in ['awdsf', 'sd', 'asdfaewsdf', 'wafds']
           if len(word) > 5)))

# q6
def capitalizer_if_under_five(listwords):
    for word in listwords:
        if len(word) < 5:
            yield word.capitalize()

print(set(capitalizer_if_under_five(['awdsf', 'sd', 'asdfaewsdf', 'wafds'])))