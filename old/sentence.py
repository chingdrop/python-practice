# Craig A. Hurley
# 2017/07/10
# sentence.py

def main():
    # Instructions to initialize the program. 
    print("This program counts how many words are in a sentence.")
    print("This program also displays the input sentence. \n")

    # The program collects the input sentence and assigns it to a variable.
    sentence = input("Please enter a sentence: ")

    # The program counts how many spaces there are in the sentence
    # and adds one for the last word which doesn't end in a space.
    count = sentence.count(" ") + 1

    # The first condition checks to see if there is a period in the sentence
    # and then prints both the sentence and the count of words. 
    if "." in sentence:
        print(count)
        print(sentence)

    # The second condition does the same as the first
    # but checks for a question mark.
    elif "?" in sentence:
        print(count)
        print(sentence)
        
    # This prints an error message if the sentnece
    # does not have a period or question mark. 
    else:
        print("Please end the sentence with a period or question mark.")
        
main()
