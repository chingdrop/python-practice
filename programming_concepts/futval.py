# File - futval.py
# Latest Version - Chapter 3
# A program to compute the value of an investment carried 10 years into the future


from programming_concepts.classes.graphics import GraphWin, Point, Rectangle, Text


def create_labeled_window():
    window = GraphWin("Investment Growth Chart", 320, 240)
    window.setBackground("white")
    window.setCoords(-1.75, -200, 11.5, 10400)
    Text(Point(-1, 0), " 0.0K").draw(window)
    Text(Point(-1, 2500), " 2.5K").draw(window)
    Text(Point(-1, 5000), " 5.0K").draw(window)
    Text(Point(-1, 7500), " 7.5k").draw(window)
    Text(Point(-1, 10000), "10.0K").draw(window)
    return window


def draw_bar(window, year, height):
    bar = Rectangle(Point(year, 0), Point(year + 1, height))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(window)


def futval_graph():
    print("This program plots the growth of a 10 year investment.")

    principal = float(input("Enter the initial principal: "))
    apr = float(input("Enter the annualized interest rate: "))

    win = create_labeled_window()
    draw_bar(win, 0, principal)
    for year in range(1, 11):
        principal = principal * (1 + apr)
        draw_bar(win, year, principal)

    input("Press <Enter> to quit.")
    win.close()


def futval():
    print("This program calculates the future value of a 10-year investment.")

    principal = float(input("Enter the initial principal: "))
    apr = float(input("Enter the annual interest rate: "))

    for i in range(10):
        principal = principal * (1 + apr)

    print(f"The value in 10 years is: {principal}")
