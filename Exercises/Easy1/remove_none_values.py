listicle = [
    None,
    'wand',
    'protude',
    None,
    'expelliarmus',
]

# newlist = list(filter(None, listicle))
newlist = list(filter(lambda word: word != None, listicle))
print(newlist)

