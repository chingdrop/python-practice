# Craig A. Hurley
# 2017/10/27
# gasMileage.py


def distance(mileInt, mileage):
    # The distance is calculated
    dist = mileInt - mileage
    return dist


def totalDistance(dist, totalDist):
    # calculates the total distance.
    totalDist = totalDist + dist
    return totalDist


def totalGas(gasUsed, gasInt):
    # calculates the total gas used.
    gasUsed = gasUsed + gasInt
    return gasUsed


def legMpg(dist, gasUsed):
    # calculates the gas mileage for the leg
    legStat = dist // gasUsed
    return legStat


def totalMpg(totalDist, gasUsed):
    # Total mileage is calculated
    totalMileage = totalDist // gasUsed
    return totalMileage


# This is the interactive module. It takes user prompts until enter is hit.
# modules above are sorted in number of occurence.
# distance, totalDistance, totalGas, legMpg, totalMpg
def interactive():

    print("You have chosen the interactive method.\n")

    # Initializes the total variables.
    gasUsed = 0.0
    totalDist = 0.0

    # Prompts the user to give an initial odometer reading.
    mileage = float(input("Enter the initial odometer reading: "))

    # Begins the sentinel loop prompting the user for the -
    # odometer reading and gas used in each leg.
    legStr = input("Enter the leg's mileage and gas used (<enter to quit>): ")

    # The loop continues until the enter is pressed.
    while legStr != "":

        # Splits the strings using a space
        mileStr, gasStr = legStr.split()

        # Converts both strings into float numbers.
        mileInt = float(mileStr)
        gasInt = float(gasStr)

        # This calls the first 3 calculation modules
        dist = distance(mileInt, mileage)
        totalDist = totalDistance(dist, totalDist)
        gasUsed = totalGas(gasUsed, gasInt)

        # The odometer is set to the new value.
        mileage = mileInt

        # LegMpg is called and printed
        legStat = legMpg(dist, gasUsed)
        print(legStat)

        # This continues the loop until enter is pressed.
        legStr = input("Enter the leg's mileage and gas used (<enter to quit>): ")

    # totalMpg is called and printed once the user hits enter.
    totalMileage = totalMpg(totalDist, gasUsed)
    print(totalMileage)


# readfile module opens a file with a name the user provides.
# readfile also uses the calculation modules above.
# distance, totalDistance, totalGas, legMpg, totalMpg
def readfile():

    print("You have selected the file method.")

    # Initializes the total variables.
    gasUsed = 0.0
    totalDist = 0.0

    # Gets a file name from the user and opens the file.
    fileName = input("what file is the leg info in? ")
    legfile = open(fileName, "r")

    # iterates through the lines in the file to collect the leg info.
    for line in legfile:

        # splits the line into two substrings.
        mileStr, gasStr = line.split()

        # converts the substrings into float numbers.
        mileInt = float(mileStr)
        gasInt = float(gasStr)

        # this is a check to determine the intial odometer reading and intial gas usage
        # the if statement checks to see if the gas usage is zero
        # if gasInt equals zero then it must be the intial reading and assigns the variable.
        if not gasInt:
            mileage = mileInt

        # the else statement tells the iteration that the following lines are leg readings.
        # not the inital reading.
        else:

            # calls the first three calculation modules.
            dist = distance(mileInt, mileage)
            totalDist = totalDistance(dist, totalDist)
            gasUsed = totalGas(gasUsed, gasInt)

            # sets the odometer to the current value.
            mileage = mileInt

            # calls the legMpg module and prints the leg statistics.
            legStat = legMpg(dist, gasUsed)
            print(legStat)

    # calls the final calculation module and prints the totalMileage.
    totalMileage = totalMpg(totalDist, gasUsed)
    print(totalMileage)

    legfile.close()


def main():

    # Prompts user for method of input.
    response = input("What method will you be using to get the information? ")

    # Checks to see if the response is valid.
    # if valid then it calls the appropriate module.
    if response[0] == "f" or response[0] == "F":
        readfile()
    elif response[0] == "i" or response[0] == "I":
        interactive()

    # if invalid then it prints an error message.
    else:
        print("Please choose a valid answer. (file or interactive)")


main()
