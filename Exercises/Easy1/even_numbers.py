# obtain only the even numbers of the list using the filter function
og_list = [1, 2, 3, 4, 5, 6]
new_list = list(filter(lambda a: a % 2 == 0, og_list))
print(new_list) # [2, 4, 6]