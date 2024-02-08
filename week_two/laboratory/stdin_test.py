from sys import stdin

rango = int(stdin.readline().strip())

user_input = stdin.readlines()
# print(user_input)

# list of cases
list_cases = []

# list of lines
list_lines = []
for e in range(len(user_input)):
    if user_input[e] != '\n':
        list_lines.append(user_input[e].strip())
        print("diferente de vacio")
    elif user_input[e] == '\n' and len(list_lines) > 0:
        list_cases.append(list_lines)
        print("igualma vacio")

        list_lines = []
    print(list_cases)

print(list_cases)

