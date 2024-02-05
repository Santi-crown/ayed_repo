

def get_lines():
    lines = []
    case_number = int(input("Write the lines number: "))

    for i in range(case_number):
        for e in range(3):
            line = input("Write the sentence please: ")
            #we get the words as a list of a sentences list
            lines.append(line.split())
        return lines

def get_letters(lista):
    word_list = []
    """for i in range(len(lista)):
        for j in range(len(lista[i])):
            for e in lista[i][j]:
                #we print each letter of the word
                print(e)

        print("")"""
    for line in lista:
        for i in range(len(line)):
            if len(line[i]) >= i:
                for j in range(len(line[i])): #There is a problem when a word don't have the lenght = to the index or is smaller.
                    if i == j:
                        word_list.append(line[i][j])
            else:
                for j in range(len(line[i])):
                    if i == j:
                        word_list.append(line[i][j])
    print(word_list)

#def message():


# def
def main():
    lines = get_lines()
    get_letters(lines)
    """print(lines)"""
main()



