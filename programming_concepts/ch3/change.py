def change():
    print("Change Counter")
    print()
    print("Please enter the count of each coin type.")

    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickels = int(input("Nickels: "))
    pennies = int(input("Pennies: "))
    total = (quarters * .25) + (dimes * .10) + (nickels * .05) + (pennies * .01)

    print()
    print("The total value of your change is", total)

if __name__ == "__main__":
    change()