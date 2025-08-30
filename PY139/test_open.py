with open('test_file.txt', 'r') as open_file:
    for line in open_file:
        print(line)

    for line in open_file:
        print(line)

with open('test_file.txt', 'a') as open_file:
    open_file.write('Hey, this is a line that I\'m appending to the file!\n')

with open('test_file.txt', 'w') as open_file:
    open_file.write('Overwriting file >:}')

open_file = open('test_file.txt', 'r')
open_file.readline()
open_file.close()