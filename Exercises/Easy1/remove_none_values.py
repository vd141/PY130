listicle = [
    None,
    'wand',
    'protude',
    None,
    'expelliarmus',
]

# remove all None values from a list using the filter method
new_listicle = list(filter(lambda a: a != None, listicle))
print(new_listicle)