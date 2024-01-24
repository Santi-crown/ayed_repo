# Exercise one

# Exercise two

# Exercise three
# region
def palindrome(word):    
    word_validation = []

    for element in range(len(word)-1,-1,-1):
        word_validation.append(word[element])
    if word == word_validation:
        print("True")
    else:
        print("False")       

def main():    
    word = input("Greetings, please type the word to see if it's a Palindrome: ")
    li_word = list(word)
    palindrome(li_word)
main()
# endregion

# Exercise four

