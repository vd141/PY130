'''
problem 1
'''
def combine(arg1, arg2, arg3):
    return (arg1, arg2, arg3)

# print(combine('1', '2', '3'))

'''
problem 2
'''
def multiply(factor1, factor2, /):
    return factor1 * factor2

# print(multiply(2, 7)) # 14
# print(multiply(factor2=2, factor1=7)) # TypeError: multiply() got some positoinal
# only arguments passed as keyword arguments

'''
problem 3
'''
def describe_pet(animal_type, /, *, name=''):
    if name:
        print(f'{name} is a {animal_type}.')
    else:
        print(f'This {animal_type} has no name.')

# describe_pet('cat', 'do', name='manny')

'''
problem 4
'''
def calculate_average(*nums):
    if not nums:
        return None
    return sum(nums) / len(nums)

# print(calculate_average(1, 2, 3, 4, 5))
# print(calculate_average())

'''
problem 5
'''
def find_person(**labor):
    for name, profession in labor.items():
        if name == 'Antonina':
            print(f'{name} is a {profession}')
            return
    print('Antonina not found.')

# find_person(bob='plumber', joe='aardvark',Antonina='Architect')

'''
problem 6
'''
def concat_strings(*all_strings, sep=' '):
    return sep.join(all_strings)

print(concat_strings('walla', 'wally', 'womash'))

'''
problem 7
'''
def register(username, /, age, *, password):
    return {'username': username, 'age': age, 'password':password}

'''
problem 8
'''
def print_message(level = 'INFO', *, message):
    print(f'{level} {message}')

print_message(message='hello')