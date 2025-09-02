# demosntrate a factory function
def add(a, b):
    return a + b

def factory_function(arg):
    def inner(new_arg):
        return add(arg, new_arg)
    
    return inner

functions = [factory_function(i) for i in range(4)]

for function in functions:
    print(function(2))