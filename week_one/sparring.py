
def get_user_input(type_input):
    if type_input == 1:
        user_input = input("Please type your input: ")
        return user_input
    else:
        number_1, number_2 = int(input("Type the first number: ")), int(input("Type the first number: "))
        return number_1, number_2

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
def gcd_two_numbers(n_1,n_2):
    while n_2 != 0:    
        n_1, n_2 = n_2, n_1 % n_2
    return n_1


def main():    
    #data
    # word = get_user_input(1)
    # word_as_list = list(word)
    n_1, n_2 = get_user_input(2)

    #Exercise one
    # character_frequency(word)

    # Exercise three
    # palindrome(word_as_list)

    # Exercise four
    gcd = gcd_two_numbers(n_1,n_2)
    print(f"The GCD of {n_1} and {n_2} is {gcd}")
main()


