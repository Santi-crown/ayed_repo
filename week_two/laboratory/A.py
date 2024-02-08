from sys import stdin

def get_lines():
    rango = int(stdin.readline().strip())
    user_input = stdin.readlines()
    # print(user_input)
    # user_input = ['\n', 'Hey good lawyer\n', 'as I previously previewed\n', 'yam does a soup\n', '\n', 'First I give money to Teresa\n', 'after I inform dad of\n', 'your horrible soup\n']
    # list of cases
    list_cases = []

    # list of lines
    list_lines = []
    # blank lines number
    blank_lines = 1
    for e in range(len(user_input)):
        if user_input[e] != '\n':
            list_lines.append(user_input[e].strip().split(' '))
            # e + 1 nos permite validar una ultima vez al final del loop para agregar el segundo caso
            if e + 1 == len(user_input):
                list_cases.append(list_lines)
        elif user_input[e] == '\n' and len(list_lines) > 0 or e == len(user_input) and len(list_lines) > 0:
            list_cases.append(list_lines)
            list_lines = []
            blank_lines += 1
        if blank_lines == rango:
            break

    return list_cases


# lines_cases = [[['Hey', 'good', 'lawyer'], ['as', 'I', 'previously', 'previewed'], ['yam', 'does', 'a', 'soup']], [['First', 'I', 'give', 'money', 'to', 'Teresa'], ['after', 'I', 'inform', 'dad', 'of'], ['your', 'horrible', 'soup']]]


def show_decoded_messaged_by_cases(list_cases):
    index = 1
    for case in list_cases:
        decodded_message = word_list(case)
        print("Case #", index)
        for message in decodded_message:
            print("".join(message))
        print("")
        index += 1

def word_list(lines):
    decoded_message_list = []
    for line in lines:
        decoded_word = []
        # index nos dirá que letra extraer y nos dara la posición de la misma en el string
        index = 0
        #if len(line) >= index:
        for word in line:
            if len(word) > index:
                decoded_word.append(word[index])
                index += 1
        decoded_message_list.append(decoded_word)

    return decoded_message_list

# def show_decodded_message(decodded_message_list):
def main():
    lines_cases = get_lines()
    show_decoded_messaged_by_cases(lines_cases)
main()