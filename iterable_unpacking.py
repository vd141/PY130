'''
practice problem 1
'''
a, b, c = (1, 2, 3)
print(a, b, c)
# 1 2 3

'''
practice problem 2
'''
a, _, c = (1, 2, 3)
# _ will be assigned to 2

'''
practice problem 3
'''
# a, b = (1, 2, 3)
# there will be an error because there are too many elements
# to be unpacked into a and b
# ValueError

'''
practice problem 4
'''
# a, b, c, d, e = (1, 2, 3)
# ValueError because there are too many variables to unpack to

'''
practice problem 5
'''
a, *rest = [1, 2, 3, 4, 5]
# rest will contain [2, 3, 4, 5]

'''
practice problem 6
'''
first, *middle, last = "hello"
print(f"First: {first}, Middle: {middle}, Last: {last}")
# the code will store the first letter in first, the last letter in last,
# and all other letters in middle

'''
practice problem 7
'''
a = 1
b = 2
b, a = a, b
print(a, b)

'''
practice problem 8
'''
((x, y), z) = ((1, 2), 3)
# x and y will be 1 and 2, respectively