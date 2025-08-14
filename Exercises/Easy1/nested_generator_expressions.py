from functools import reduce

listolists = [
    [1, 2, 3, 4],
    [6, 7, 8],
    [9, 6, 4],
    [1, 6, 4],
]

# loop through each nested list and add it to a new list
new_list = (num
            for sublist in listolists
            for num in sublist)
print(list(new_list))