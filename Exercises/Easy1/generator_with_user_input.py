def gen_user_input():
    while True:
        user_in = input('Enter something: ')
        if user_in != 'stop':
            yield user_in
        else:
            break

a = gen_user_input()

for inputty in a:
    print(inputty)