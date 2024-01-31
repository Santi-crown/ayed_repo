import os

def delete_screen():
    if os.name == "posix":
        os.system("clear" )
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")

def menu():
        print ("Selecciona una opción")
        print ("\t1 - Character frequency")
        print ("\t2 - Wonder Square")
        print ("\t3 - Palindrome string")
        print ("\t4 - Greatest Common Diviso")
        print ("\t5 - salir")

def get_user_input(type_input):
    if type_input == 1:
        user_input = input("Please type your string: ")
        return user_input
    elif type_input == 2:
        number_1, number_2 = int(input("Type the first number: ")), int(input("Type the first number: "))
        return number_1, number_2
    else:
        user_input = -1
        while user_input < 0:
            user_input = int(input("Type the size, please: "))
        return user_input

# 1. 
def character_frequency(word):
    times = 0
    most_frequently = ""
    for ci in word:
        frequently_ci = count(ci,word)
        if frequently_ci > times:
            times = frequently_ci
            most_frequently = ci
    
    print(most_frequently, "--->",times)

# We need a function that allow us to count the occurrences of ci within the word
def count(ci,word):
    frequency = 0
    for c in word:        
        if c == ci:
            frequency = frequency + 1
    return frequency

# 2. 
def generate_wonder_square(n):
    # This is because we need the matrix to be of odds size so it can form the WonderSquare
    size = 2 * n - 1

    # Here we're initializing the 0 matrix with the odd size
    matriz = [[0 for i in range(size)] for j in range(size)]

    # Here we are going to fill the matrix. 
    for i in range(n):  
        for j in range(i, size - i):
            matriz[i][j] = matriz[j][i] = matriz[size - i - 1][j] = matriz[j][size - i -1] = n - i
    return matriz

def print_wonder_square(wonder_square):
    for row in wonder_square:
        print(" ".join(map(str, row)))


# 3. 
def palindrome(word):    
    word_validation = []
    for element in range(len(word)-1,-1,-1):
        word_validation.append(word[element])
    if word == word_validation:
        print("True")
    else:
        print("False")       

# 4. 
# Euclidean Algorithm 
# This algorithm repeatedly divides the larger number by the smaller number and assigns the remainder as the new divisor until the remainder becomes zero. Then, the last non-zero remainder is the gcd.
def gcd_two_numbers(n_1,n_2):
    while n_2 != 0:    
        n_1, n_2 = n_2, n_1 % n_2
    return n_1


def main():    
    while True:
        menu()
        opcionMenu = input("inserta un numero valor >> ")

        if opcionMenu=="1":
            # 1. 
            word = get_user_input(1)
            word_as_list = list(word)
            character_frequency(word)
            input("Ha seleccionado la opción 1...\npulsa una tecla para continuar ")
        elif opcionMenu=="2":            
            # 2. 
            # here we generate the matrix
            n = get_user_input(3)
            wonder_square = generate_wonder_square(n)
            # Here, we give it a print format
            print_wonder_square(wonder_square)
            input("Ha seleccionado la opción 2...\npulsa una tecla para continuar")

        elif opcionMenu=="3":
            # 3.  
            word = get_user_input(1)
            string_as_list = list(word)        
            palindrome(word_as_list)                        
            input("Ha seleccionado la opción 3...\npulsa una tecla para continuar")

        elif opcionMenu=="4":        
            # 4.
            n_1, n_2 = get_user_input(2)
            gcd = gcd_two_numbers(n_1,n_2)
            print(f"The GCD of {n_1} and {n_2} is {gcd}")
            input("Ha seleccionado la opción 4...\npulsa una tecla para continuar")

        elif opcionMenu=="5":
            input("Ha seleccionado la opción 5...\npulsa una tecla para continuar")
            print("Chao Chao")
            break
main()