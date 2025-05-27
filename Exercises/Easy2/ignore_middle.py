'''
unpack values from a tuple of four elements, but only keep the first and last values
'''


data = (100, 200, 300, 400)

first, _, _, last = data
print(first, last)