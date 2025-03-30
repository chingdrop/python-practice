from src.calc import distance
from src.classes.graphics import Entry, GraphWin, Point, Polygon, Text


def click():
    win = GraphWin("Click Me!")
    for i in range(10):
        p = win.getMouse()
        print(f"You clicked at: {p.getX()}, {p.getY()}")


def click_and_type():
    win = GraphWin("Click and Type", 400, 400)
    for i in range(10):
        pt = win.getMouse()
        key = win.getKey()
        field = Text(pt, key)
        field.draw(win)


def handle_key(k, win):
    if k == "r":
        win.setBackground("pink")
    elif k == "w":
        win.setBackground("white")
    elif k == "g":
        win.setBackground("lightgray")
    elif k == "b":
        win.setBackground("lightblue")


def handle_click(pt, win):
    # create an Entry for user to type in
    entry = Entry(pt, 10)
    entry.draw(win)

    # Go modal: wait until user types Return or Escape Key
    while True:
        key = win.getKey()
        if key == "Return":
            break

    # undraw the entry and draw Text
    entry.undraw()
    Text(pt, entry.getText()).draw(win)

    # clear (ignore) any mouse click that occurred during text entry
    win.checkMouse()


def event_loop():
    win = GraphWin("Click and Type", 500, 500)

    # Event Loop: handle key presses and mouse clicks until the user
    #    presses the "q" key.
    while True:
        key = win.checkKey()
        if key == "q":  # loop exit
            break

        if key:
            handle_key(key, win)

        pt = win.checkMouse()
        if pt:
            handle_click(pt, win)

    win.close()


def triangle():
    win = GraphWin("Draw a Triangle")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points")
    message.draw(win)

    # Get and draw three vertices of triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    # Use Polygon object to draw the triangle
    triangle = Polygon(p1, p2, p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)

    # Calculate the perimeter of the triangle
    perim = distance(p1, p2) + distance(p2, p3) + distance(p3, p1)
    message.setText(f"The perimeter is: {perim:0.2f}")

    # Wait for another click to exit
    win.getMouse()
    win.close()