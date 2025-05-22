file = open('example.txt', 'r')
# content = file.read()

# print(content)
# print(repr(content))

# content2 = file.readlines()
# print(content2)

# file.close()
print(type(file))

result = '_'
while result != repr(''):
    result = repr(file.readline())
    print(result)

file.close()

# Don't use a REPL to run this code
file = open('output.txt', 'w')
file.write('Hello, world!\n')

lines = ['First line\n', 'Second line\n']
file.writelines(lines)

file.close()

# Don't use a REPL to run this code
# file = open('output.txt', 'a')
# file.write('Third line!\n')
# file.write('Last line!\n')
# file.close()

# newfile = open('example.txt', 'r')
# for line in newfile:
#     print(line)
# newfile.close()

with open('example.txt', 'r') as newfile:
    for line in newfile:
        print(line)