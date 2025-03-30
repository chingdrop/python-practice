# File - event_loop.py
# Version 3
# Latest Version - Chapter 8
# Color changing window with clicks to enter text

from programming_concepts.classes.graphics import *


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


def main():
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


if __name__ == "__main__":
    main()
