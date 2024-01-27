
def get_user_input():
    user_input = input("Please type your input: ")
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
# Exercise three

def palindrome(word):    
    word_validation = []
    for element in range(len(word)-1,-1,-1):
        word_validation.append(word[element])
    if word == word_validation:
        print("True")
    else:
        print("False")       

def main():    
    #data
    word = get_user_input()
    word_as_list = list(word)

    #Exercise one
    character_frequency(word)

    # Exercise three
    # palindrome(word_as_list)
main()

# Exercise four


