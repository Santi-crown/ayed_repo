

def get_lines():
    lines = []
    case_number = int(input("Write the lines number: "))

    for i in range(case_number):
        for e in range(3):
            line = input("Write the sentence please: ")
            #we get the words as a list of a sentences list
            lines.append(line.split())
        return lines

def get_letter_as_list(lista):
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            for e in lista[i][j]:
                #we print each letter of the word
                print(e)
                """print(lista[i][j])"""
        print("")


# def
def main():
    lines = get_lines()
    get_letter_as_list(lines)
    """print(lines)"""
main()



