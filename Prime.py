# Craig Hurley
# 2017/1/12
# Prime.py

def makeCheckList(n):
    # This method creates a list and fills it with numbers starting with 2
    # and ending with the limit.
    checkList = []
    for i in range(2, n+1):
        checkList.append(i)
    return checkList

def checkPrime(checkList, n):
    primeList = []
    # Iterates through the checkList
    while checkList:
        # assigns the element currently used and adds it to the primeList
        num = checkList[0]
        primeList.append(num)
        # Determines multiples using a for loop.
        # starts at the current element and ends at the limit in steps of num
        for j in range(num, n+1, num):
            # Checks to see if the multiple is in the check List.
            # Removes the multiple from check list.
            if j in checkList:
                checkList.remove(j)
    return primeList
            
def main():

    print("This program determines all prime numbers between 2 and the input limit.")
    print()
    # Prompts the user to enter in the limit.
    n = int(input("Enter the number you wish to be the limit: "))
    # calls the fill check list method with the desired limit.
    check = makeCheckList(n)
    # calls the comb method that iterates through the list removing multiples
    # and adding the element to the prime list.
    prime = checkPrime(check, n)
    # prints the primeList
    print("-" * 50)
    print(prime)

main()
