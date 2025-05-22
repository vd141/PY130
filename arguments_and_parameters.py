'''
question 1
'''
def combine(pos1, pos2, pos3):
    return (pos1, pos2, pos3)

# print(combine('hey', 'i', 'just'))

'''
question 2
'''
def multiply(pos1, pos2, /):
    return pos1 * pos2

# print(multiply(3, 4))

'''
question 3
'''
def describe_pet(animal_type, *, name=''):
    print(f'{name} is an {animal_type}')

# describe_pet('Cuttlefish', name='Jimmy')

'''
question 4
'''
def calculate_average(*nums):
    return sum(nums) / len(nums) if nums else None

# print(calculate_average(range(45, 89)))

'''
question 5
'''
def find_person(**pairs):
    if 'Antonina' in pairs:
        print(f'Antonina is a {pairs['Antonina']}')
    else:
        print('Antonina not found.')

# find_person(Antonina='SWE', James='Lebron James')

'''
question 6
'''
def concat_strings(*strings, sep=' '):
    return sep.join(strings)

print(concat_strings(*'asdfaweds'))

'''
question 7
'''
def register(username, /, age, *, password):
    return f'{username}\'s age ({age}) and password ({password}).'

# print(register('danny', age=4, password='@!#$12'))

'''
question 8
'''
def print_message(level='INFO', *, message):
    print(level + message)

print_message(message='This is a shoutout.', level='PLUS: ')