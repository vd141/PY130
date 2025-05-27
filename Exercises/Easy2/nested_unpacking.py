'''
write some code to unpack the nested tuple into individual variables
a, b, c, d, e, f
'''
data = ((1, 2), (3, 4), (5, 6))
((a, b), (c, d), (e, f)) = data
print(a, b, c, d, e, f)