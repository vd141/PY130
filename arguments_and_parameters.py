'''
write a function named combine that takes three positional arguments and returns
a tuple containing all three. call this function with three different values
'''

def combine(arg1, arg2, arg3):
    return (arg1, arg2, arg3)
print(combine(1, 2, 43))

'''
define a function named multiply that accepts two positional only arguments
and returns their product. the function should not allow these arguments to be
passed in as keyword arguments
'''
def multiply(arg1, arg2, /):
    return arg1 * arg2
print(multiply(2, 3))
# print(multiply(arg1 = 2, arg2 = 3))

'''
generate a function named describe_pet that takes one positional argument animal_type
and one keyword argument name with a default value of an empty string. the function
should print a description of a pet. the function should not accept more than 1 positional
argument
'''
def describe_pet(animal_type, *, name=''):
    print(f'{name} is an {animal_type}')

describe_pet('cat', name='John')
describe_pet(animal_type='cat', name='John')

'''
write a function named calculate average that takes any number of numeric arguments
and returns their average. make sure it returns none if no arguments are provided
'''
def calculate_average(*numbers):
    if numbers:
        return sum(numbers) / len(numbers)
    
print(calculate_average(*(range(1, 5))))
print(calculate_average())

'''
Create a function named find_person that accepts any number of keyword arguments 
in which each key is someone's name and the value is their associated profession. 
The function should check whether any of the key/value pairs has a key of "Antonina" 
and then, if the key is found, print a message that shows Antonina's profession. 
Otherwise, it should say "Antonina not found". The function should not accept any 
positional arguments.
'''
def find_person(**kwargs):
    for name, profession in kwargs.items():
        if name == 'Antonina':
            print(f'{name}\'s profession is {profession}.')
            return
    print('Antonina not found')

find_person(John="Engineer", Antonina="Software Engineer")
# Antonina's profession is Software Engineer

find_person(John="Engineer", Ginni="Software Engineer")
# Antonina not found

'''
write a function named concat_strings that takes any number of strings and
returns the concatenation of all the strings. add a keyword only argument sep with
a default value of ' ' that specifies the separator to use between the strings
'''
def concat_strings(sep = ' ', *words):
    return sep.join(words)

'''
Create a function named register that takes exactly three arguments: username as 
positional-only, password as keyword-only, and age as either a positional or 
keyword argument.
'''
def register(username, /, age, *, password):
    pass

'''
Create a function named print_message that requires a keyword-only argument 
(message) and an optional keyword-only argument (level) with a default value of 
"INFO". The function should print out the message prefixed with the level. The 
function shouldn't accept any positional arguments.
'''
def print_message(*, level='INFO', message):
    print(f'{level}: {message}')

print_message(message='tripe', level='WARNING')

# closures practice
def notify(message, when):
    print(f"{message} in {when} minutes!")

def later2(func, first_arg):
    def inner(second_arg):
        return func(first_arg, second_arg)
    
    return inner

shutdown_warning = later2(notify, "The system is shutting down")
shutdown_warning(30) # The system is shutting down in 30 minutes!