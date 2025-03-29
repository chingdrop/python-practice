# Craig A. Hurley
# 2017/08/10
# namecount.py

def main():

    # The program prompts the user for his/her first and last name.
    firstName = input("Please enter your first name: ")
    lastName = input("Please enter last name: ")

    # Since the program uses the Unicode value for lowercase characters only
    # the program replaces the old string with the new lowercase string. 
    firstName = firstName.lower()
    lastName = lastName.lower()

    # The values of the totals must be initialized to 0.
    total1 = 0
    total2 = 0

    # Iterator #1 goes through the characters of the first name
    # and assigns the value in the alphabet using Unicode.
    for ch in firstName:
        fch = (ord(ch) - 96)
        total1 = total1 + fch

    # Iterator #2 goes through the characters of the last name
    # and assigns the value in the alphabet using Unicode.
    for ch in lastName:
        lch = (ord(ch) - 96)
        total2 = total2 + lch
    
    # The program then prints the value of the first name,
    # the value of the last name, and the value of the combined name. 
    print("First name: {0}".format(total1))
    print("Last name: {0}".format(total2))
    print("Combined name: {0}".format(total1 + total2))

main()
