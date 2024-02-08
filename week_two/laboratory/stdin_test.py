from sys import stdin

rango = int(stdin.readline().strip())
# rango = 2
# No esta tomando en cuenta el rango

user_input = stdin.readlines()
# print(user_input)
# user_input = ['\n', 'Hey good lawyer\n', 'as I previously previewed\n', 'yam does a soup\n', '\n', 'First I give money to Teresa\n', 'after I inform dad of\n', 'your horrible soup\n']
#list of cases
list_cases = []

#list of lines
list_lines = []

print(len(user_input))
# blank lines number
blank_lines = 1
for e in range(len(user_input)):
    print(user_input[e])
    if user_input[e] != '\n':
        list_lines.append(user_input[e].strip().split(' '))
        # e + 1 nos permite validar una ultima vez al final del loop para agregar el segundo caso
        if e+1 == len(user_input):
            list_cases.append(list_lines)
    elif user_input[e] == '\n' and len(list_lines) > 0 or e == len(user_input) and len(list_lines) > 0:
        list_cases.append(list_lines)
        list_lines = []
        blank_lines += 1
    #print(list_cases)

print(list_cases)

