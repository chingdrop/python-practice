# File - clickntype.py
# Latest Version - Chapter 4
# Graphics program illustrating mouse and keypress inputs

from graphics import *

def main():
    win = GraphWin("Click and Type", 400, 400)
    for i in range(10):
        pt = win.getMouse()
        key = win.getKey()
        field = Text(pt, key)
        field.draw(win)
    
main()
