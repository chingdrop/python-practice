#threecardmonte.py

from graphics import GraphWin, Point
from button import Button
from random import randrange

def main():

    #Create the game view window
    win = GraphWin("GameView")
    win.setCoords(0, 0, 10, 10)
    win.setBackground("green2")

    winCount = 0
    loseCount = 0
    correct = randrange(1,4)
    choice = 0

    # draw the buttons
    cb1 = Button(win, Point(1.75,3), 3, 5, "Option 1")
    cb1.activate()
    cb2 = Button(win, Point(5.125,3), 3, 5, "Option 2")
    cb2.activate()
    cb3 = Button(win, Point(8.5,3), 3, 5, "Option 3")
    cb3.activate()
    qb = Button(win, Point(8.5,9), 3, 1, "Quit")

    pt = win.getMouse()
    
    while not qb.clicked(pt):
        
        if cb1.clicked(pt):
            choice = 1
        elif cb2.clicked(pt):
            choice = 2
        elif cb3.clicked(pt):
            choice = 3

        if choice == correct:
            winCount = winCount + 1
            print("you win, keep going or quit")
        else:
            loseCount = loseCount + 1
            print("you lose, keep going or quit")

        qb.activate()
        pt = win.getMouse()
        
    wMessage = str(winCount)
    lMessage = str(loseCount)
    print("you won "+wMessage+" times.")
    print("you lost "+lMessage+" times.")
    win.close()

main()
