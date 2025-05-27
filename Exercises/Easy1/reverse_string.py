astring = 'make this backwards'
new_gen = (letter for letter in astring[::-1])

print(''.join(new_gen))