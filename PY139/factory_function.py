def double(num):
    return num * 2

def factory_function(n):
    def inner():
        return double(n)
    
    return inner

functions = [factory_function(n) for n in range(1, 12)]

for function in functions:
    print(function())

new_funcs = []
for i in range(1, 12):
    new_funcs.append(lambda n=i: n * 2)

for function in new_funcs:
    print(function())