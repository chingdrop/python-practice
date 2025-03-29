import random


# Create a new class to handle all methods called from main().
class List:

    # Creates the constructor which creates a list on startup.
    def __init__(self):

        self.initList = []

    # This method fills the empty list with 20 random digits between 1 and 100.
    def createList(self):

        # Assigns the constructor list to a new variable.
        newList = self.initList
        # Uses iteration to create 20 random numbers.
        for x in range(20):
            # Random numbers from 1 to 100 are assigned to the element variable.
            newRandom = random.randint(1, 100)
            # The random number is appended to the list.
            newList.append(newRandom)
        # The method returns the list filled with the new entries.
        return newList

    # This method reverses the list by using slicing.
    def reverseList(self, listVal):

        # Returns a copy of the first list but reversed by using slicing.
        return listVal[::-1]

    # This method calculates the big O efficiency for the program.
    def bigOCalc(self, listVal):

        # Since a copy is created the formula O(n) is used.
        # This is linear with the number of entries to the list.
        n = len(listVal)
        # The slicing effort is a different integer than the length of the list.
        # Since the entire list is sliced, the length of the list is used.
        k = n
        # Returns the bigO efficiency.
        return n + k


def main():

    # The class is loaded under the randomList variable.
    randomList = List()
    # To create the inital list, the createList method is called.
    beforeList = randomList.createList()
    # To reverse the initial list, the reverseList method is given the initial list as a parameter.
    afterList = randomList.reverseList(beforeList)
    # To calculate the bigO, the bigOCalc method is given the reversed list as a parameter.
    bigOList = randomList.bigOCalc(afterList)

    # These statements turn data objects into strings, and prints the output from the program.
    print(str(beforeList))
    print(str(afterList))
    print(str(bigOList))


main()
