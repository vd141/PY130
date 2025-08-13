# create a list where each number from the original list is squared using the
# map method

og_list = [1, 2, 3, 4, 5]
new_list = list(map(lambda a: a ** 2, og_list))
print(new_list) # 1, 4, 9, 16, 25