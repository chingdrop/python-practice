# File - click.py
# Latest Version - Chapter 4
from programming_concepts.graphics import *


def main():
    win = GraphWin("Click Me!")
    for i in range(10):
        p = win.getMouse()
        print(f"You clicked at: {p.getX()}, {p.getY()}")


if __name__ == "__main__":
    main()
