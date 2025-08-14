# create a basic generator function that yields numbers from 1 to 5

def gen_func():
    for i in range(1, 6):
        yield i

for i in gen_func():
    print(i)