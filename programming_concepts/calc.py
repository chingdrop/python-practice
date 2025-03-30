import math
from math import sqrt

from programming_concepts.classes.graphics import *
from programming_concepts.classes.button import Button


# Latest Version - Chapter 11
# A four function calculator using Python arithmetic.
# Illustrates use of objects and lists to build a simple GUI.


class Calculator:
    # This class implements a simple calculator GUI

    def __init__(self):
        # create the window for the calculator
        win = GraphWin("calculator")
        win.setCoords(0, 0, 6, 7)
        win.setBackground("slategray")
        self.win = win
        # Now create the widgets
        self.__create_buttons()
        self.__create_display()

    def __create_buttons(self):
        # create list of buttons
        # start with all the standard sized buttons
        # bSpecs gives center coords and label of buttons
        b_specs = [
            (2, 1, "0"),
            (3, 1, "."),
            (1, 2, "1"),
            (2, 2, "2"),
            (3, 2, "3"),
            (4, 2, "+"),
            (5, 2, "-"),
            (1, 3, "4"),
            (2, 3, "5"),
            (3, 3, "6"),
            (4, 3, "*"),
            (5, 3, "/"),
            (1, 4, "7"),
            (2, 4, "8"),
            (3, 4, "9"),
            (4, 4, "<-"),
            (5, 4, "C"),
        ]
        self.buttons = []
        for cx, cy, label in b_specs:
            self.buttons.append(Button(self.win, Point(cx, cy), 0.75, 0.75, label))
        # create the larger = button
        self.buttons.append(Button(self.win, Point(4.5, 1), 1.75, 0.75, "="))
        # activate all buttons
        for b in self.buttons:
            b.activate()

    def __create_display(self):
        bg = Rectangle(Point(0.5, 5.5), Point(5.5, 6.5))
        bg.setFill("white")
        bg.draw(self.win)
        text = Text(Point(3, 6), "")
        text.draw(self.win)
        text.setFace("courier")
        text.setStyle("bold")
        text.setSize(16)
        self.display = text

    def get_button(self):
        # Waits for a button to be clicked and returns the label of
        #    the button that was clicked.
        while True:
            p = self.win.getMouse()
            for b in self.buttons:
                if b.clicked(p):
                    return b.getLabel()  # method exit

    def process_button(self, key):
        # Updates the display of the calculator for press of this key
        text = self.display.getText()
        if key == "C":
            self.display.setText("")
        elif key == "<-":
            # Backspace, slice off the last character.
            self.display.setText(text[:-1])
        elif key == "=":
            # Evaluate the expresssion and display the result.
            # the try...except mechanism "catches" errors in the
            # formula being evaluated.
            try:
                result = eval(text)
            except:
                result = "ERROR"
            self.display.setText(str(result))
        else:
            # Normal key press, append it to the end of the display
            self.display.setText(text + key)

    def run(self):
        # Infinite 'event loop' to process button clicks.
        while True:
            key = self.get_button()
            self.process_button(key)


# Version 3
# Latest Version - Chapter 6


def add_interest(balances, rate):
    for i in range(len(balances)):
        balances[i] = balances[i] * (1 + rate)


# Version 7
# Latest Version - Chapter 8


def average():
    file_path = input("What file are the numbers in? ")
    with open(file_path, "r") as input_file:
        total = 0.0
        count = 0
        line = input_file.readline()
        while line != "":
            # update total and count for values in line
            for x_str in line.split(","):
                total = total + float(x_str)
                count = count + 1
            line = input_file.readline()
        print(f"\nThe average of the numbers is {total / count}")


# Version 3
# Latest Version - Chapter 5
# A program to calculate the value of some change in dollars
# This version represents the total cash in cents.


def calc_change_total():
    print("Change Counter\n")
    print("Please enter the count of each coin type.")

    quarters = int(input("Quarters: "))
    dimes = int(input("Dimes: "))
    nickels = int(input("Nickels: "))
    pennies = int(input("Pennies: "))
    total = quarters * 25 + dimes * 10 + nickels * 5 + pennies

    print(f"The total value of your change is ${total // 100}.{total % 100:0>2}")


# Latest Version - Chapter 3
# Program to compute the factorial of a number
# Illustrates for loop with an accumulator


def factorial():
    n = int(input("Please enter a whole number: "))
    fact = 1
    for factor in range(n, 1, -1):
        fact = fact * factor
    print(f"The factorial of {n} is {fact}")


# Latest Version - Chapter 7
# Finds the maximum of a series of numbers


def maxn():
    n = int(input("How many numbers are there? "))

    # Set max to be the first value
    maxn = float(input("Enter a number: "))

    # Now compare the n-1 successive values
    for i in range(n - 1):
        x = float(input("Enter a number: "))
        if x > maxn:
            maxn = x

    print(f"The largest value is {maxn}")


def quadratic():
    print("This program finds the real solutions to a quadratic\n")

    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))
        disc_root = math.sqrt((b * b) - (4 * a * c))
        root1 = (-b + disc_root) / (2 * a)
        root2 = (-b - disc_root) / (2 * a)
        print(f"\nThe solutions are: {root1}, {root2}")
    except ValueError as e:
        if str(e) == "math domain error":
            print("No Real Roots")
        else:
            print("Invalid coefficient given")
    except:
        print(f"\nUnexpected Error: {e}")


def get_numbers():
    nums = []  # start with an empty list

    # sentinel loop to get numbers
    x = input("Enter a number (<Enter> to quit) >> ")
    while x != "":
        x = float(x)
        nums.append(x)  # add this value to the list
        x = input("Enter a number (<Enter> to quit) >> ")
    return nums


def mean(nums):
    total = 0.0
    for num in nums:
        total = total + num
    return total / len(nums)


def std_dev(nums, xbar):
    sum_dev_sq = 0.0
    for num in nums:
        dev = num - xbar
        sum_dev_sq = sum_dev_sq + dev * dev
    return sqrt(sum_dev_sq / (len(nums) - 1))


def median(nums):
    nums.sort()
    size = len(nums)
    mid_pos = size // 2
    if size % 2 == 0:
        med = (nums[mid_pos] + nums[mid_pos - 1]) / 2.0
    else:
        med = nums[mid_pos]
    return med