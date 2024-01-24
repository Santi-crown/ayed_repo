# Exercise one

# Exercise two

# Exercise three
def palindrome(word):

    # # print(word)
    # word_validation = []
    # word_validation = word
    # word_validation.reverse()
    # # re_word = word.reverse()

    # print(word_validation)
    # print(word)

    # # print(re_word," XD")
    
    word_validation = []

    for element in range(len(word)-1,-1,-1):
        word_validation.append(word[element])
        # print(word[element])
    if word == word_validation:
        print("True")
    else:
        print("False")
    
    print(word)
    print(len(word))
    print(word_validation)

# Exercise four
def main():
    
    word = input("Greetings, please type the word to see if it's a Palindrome: ")

    li_word = list(word)

    palindrome(li_word)
    
    # print(word)
main()

