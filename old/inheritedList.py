# Craig Hurley
# 2017/11/17
# COP2030 Assignment 8
# inheritedList.py


from random import randrange

class MasterList:
    # The original number list (repeatable numbers).

    def __init__(self):
        # Create a master list filled with 50 random numbers between 1 - 100
        self.masterList = [randrange(1,101) for i in range(50)]
        

    def getMasterList(self):
        # Returns the masterList as an iteration.
        return self.masterList[:]

class UniqueList:
    # The list filled with only unique numbers.

    def __init__(self, masterList):
        # Copies masterList by assigning it to uniqueList.
        # Removes the duplicate numbers from masterList.
        self.uniqueList = masterList
        self.uniqueList = list(set(masterList))

    def getUniqueList(self):
        # Returns the uniqueList as an iteration.
        return self.uniqueList[:]

def main():
    
    # Starts the program by starting the classes.
    masterList = MasterList()
    # Since uniqueList uses MasterList I made it use the return method.
    uniqueList = UniqueList(masterList.getMasterList())

    # Prints the info message and the lists.
    print("This is the original list with repeating numbers.")
    print(masterList.getMasterList())
    print("This is the sorted list with only unique numbers.")
    print(uniqueList.getUniqueList())

main()
