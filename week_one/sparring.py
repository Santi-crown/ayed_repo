
def get_user_input(type_input):
    if type_input == 1:
        user_input = input("Please type your input: ")
        return user_input
    elif type_input == 2:
        number_1, number_2 = int(input("Type the first number: ")), int(input("Type the first number: "))
        return number_1, number_2
    else:
        user_input = -1
        while user_input < 0:
            user_input = int(input("Type the size, please: "))
        return user_input

# Exercise one
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

# Exercise two
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



# Exercise three
def palindrome(word):    
    word_validation = []
    for element in range(len(word)-1,-1,-1):
        word_validation.append(word[element])
    if word == word_validation:
        print("True")
    else:
        print("False")       

# Exercise four
# Euclidean Algorithm 

# This algorithm repeatedly divides the larger number by the smaller number and assigns the remainder as the new divisor until the remainder becomes zero. Then, the last non-zero remainder is the gcd.
def gcd_two_numbers(n_1,n_2):
    while n_2 != 0:    
        n_1, n_2 = n_2, n_1 % n_2
    return n_1


def main():    
    #data
    # word = get_user_input(1)
    # word_as_list = list(word)

    # n_1, n_2 = get_user_input(2)

    n = get_user_input(3)

# - - - - -- - 

    # 1. Exercise one
    # character_frequency(word)

    # 2. Exercise two
    # here we generate the matrix
    wonder_square = generate_wonder_square(n)
    # Here, we give it a print format
    print_wonder_square(wonder_square)


    # 3.  Exercise three
    # palindrome(word_as_list)

    # 4.  Exercise four
    # gcd = gcd_two_numbers(n_1,n_2)
    # print(f"The GCD of {n_1} and {n_2} is {gcd}")

main()


