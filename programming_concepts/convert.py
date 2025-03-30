# File - convert.py
# Version - 2
# Latest Version - Chapter 7
# A program to convert Celsius temps to Fahrenheit.
# This version issues heat and cold warnings.


from programming_concepts.classes.graphics import (
    Entry,
    GraphWin,
    Point,
    Rectangle,
    Text,
)


def convert():
    celsius = float(input("What is the Celsius temperature? "))
    fahrenheit = (9 / 5) * celsius + 32
    print(f"The temperature is {fahrenheit} degrees Fahrenheit.")

    # Print warnings for extreme temps
    if fahrenheit > 90:
        print("It's really hot out there. Be careful!")
    if fahrenheit < 30:
        print("Brrrrr. Be sure to dress warmly!")


def connect_gui():
    win = GraphWin("Celsius Converter", 400, 300)
    win.setCoords(0.0, 0.0, 3.0, 4.0)

    # Draw the interface
    Text(Point(1, 3), "   Celsius Temperature:").draw(win)
    Text(Point(1, 1), "Fahrenheit Temperature:").draw(win)
    inputText = Entry(Point(2.25, 3), 5)
    inputText.setText("0.0")
    inputText.draw(win)
    outputText = Text(Point(2.25, 1), "")
    outputText.draw(win)
    button = Text(Point(1.5, 2.0), "Convert It")
    button.draw(win)
    Rectangle(Point(1, 1.5), Point(2, 2.5)).draw(win)

    # wait for a mouse click
    win.getMouse()

    # convert input
    celsius = float(inputText.getText())
    fahrenheit = (9.0 / 5.0) * celsius + 32

    # display output and change button
    outputText.setText(round(fahrenheit, 2))
    button.setText("Quit")

    # wait for click and then quit
    win.getMouse()
    win.close()


# Version 2
# Latest Version - Chapter 5
# Converts day month and year numbers into two date formats


def date_convert():
    # get the day month and year as numbers
    day = int(input("Enter the day number: "))
    month = int(input("Enter the month number: "))
    year = int(input("Enter the year: "))

    date1 = f"{str(month)} / {str(day) / {str(year)}}"

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    month_str = months[month - 1]
    date2 = f"{month_str} {str(day)}, {str(year)}"

    print(f"The date is: {date1} or {date2}.")


# Version 2
# Latest Version - Chapter 5
# A program to convert a sequence of Unicode numbers into a string of text.
# Efficient version using a list accumulator.


def int_to_str():
    print(
        "This program converts a sequence of Unicode numbers into the string of text that it represents.\n"
    )

    # Get the message to encode
    input_str = input("Please enter the Unicode-encoded message: ")

    # Loop through each substring and build Unicode message
    chars = []
    for num_str in input_str.split():
        code_num = int(num_str)  # convert digits to a number
        chars.append(chr(code_num))  # accumulate new character

    message = "".join(chars)
    print(f"\nThe decoded message is: {message}")


# Latest Version - Chapter 5
# A program to convert a textual message into a sequence of numbers, utilizing the underlying Unicode encoding.


def str_to_int():
    print(
        "This program converts a textual message into a sequence of numbers representing the Unicode encoding of the message.\n"
    )

    # Get the message to encode
    message = input("Please enter the message to encode: ")

    print("\nHere are the Unicode codes:")

    # Loop through the message and print out the Unicode values
    for ch in message:
        print(ord(ch), end=" ")

    print()  # End line of output