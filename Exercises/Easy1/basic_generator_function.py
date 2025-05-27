def yield_1_to_5():
    for i in range(1, 6):
        yield i

a = yield_1_to_5()

for num in a:
    print(num)