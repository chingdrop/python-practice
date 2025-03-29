# File - change.py
# Version 3
# Latest Version - Chapter 5
# A program to calculate the value of some change in dollars
# This version represents the total cash in cents.


def main():
    print("Change Counter\n")
    print("Please enter the count of each coin type.")

    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickels = int(input("Nickels: "))
    pennies = int(input("Pennies: "))
    total = quarters * 25 + dimes * 10 + nickels * 5 + pennies

    print(f"The total value of your change is ${total // 100}.{total % 100:0>2}")


if __name__ == "__main__":
    main()
