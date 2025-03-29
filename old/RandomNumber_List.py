import random

def main():
    randomList = []
    for x in range(20):
        newElement = random.randint(1,101)
        randomList.append(newElement)

    print(randomList)

main()
