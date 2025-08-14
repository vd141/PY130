# create a generator function that yields user input strings until the word "stop" is 
# entered

def gen_input():
    while True:
        user_inp = input('Enter something: ')
        if user_inp == 'stop':
            break
        yield user_inp

for user_input in gen_input():
    print(user_input)