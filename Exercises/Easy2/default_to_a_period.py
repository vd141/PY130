def greet(name, greeting, punctuation='.'):
    return f'{greeting}, {name}{punctuation}'

print(greet("Antonina", "Hello")) # Hello, Antonina.
print(greet("Pete", "Good morning", "!")) # Good morning, Pete!