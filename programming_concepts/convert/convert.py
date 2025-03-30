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
