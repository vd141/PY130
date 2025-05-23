'''
question 2
'''
def make_counter():
    def counter_func():
        counter = 0
        counter += 1
        return counter

    return counter_func

# increment_counter = make_counter()
# print(increment_counter())
# print(increment_counter())

# increment_counter = make_counter()
# print(increment_counter())
# print(increment_counter())

'''
question 3
'''
from functools import partial

def greet(name, greeting):
    return f"{greeting}, {name}!"

# say_hello_to = partial(greet, greeting="Hello")
# print(say_hello_to(name="Alice"))  # What will this print?

'''
question 4
'''
def later(func, argument):
    def inner():
        return func(argument)
    return inner

def printer(message):
    print(message)

print_warning = later(printer, "The system is shutting down!")
print_warning()  # The system is shutting down!

'''
question 5
'''
def later2(func, first_arg):
    
    def inner(second_arg):
        return func(first_arg, second_arg)

    return inner

def notify(message, when):
    print(f"{message} in {when} minutes!")

shutdown_warning = later2(notify, "The system is shutting down")
shutdown_warning(30) # The system is shutting down in 30 minutes!