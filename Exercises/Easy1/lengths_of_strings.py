words = [
    'abe',
    'barnus',
    'pottery',
    'flume',
    'hundreds',
    'poultry',
    'limerance',
    'loquacious',
]

# use map to create a list of lengths of strings
lengths = list(map(lambda a: len(a), words))
# more pythonic:
lengths = list(map(len, words))
print(lengths) # [3, 6, 7, 5..]