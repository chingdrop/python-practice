# Craig Hurely
# 2017/11/02
#threecardmonte.py

from random import randrange
from programming_concepts.classes.graphics import GraphWin, Point
from programming_concepts.classes.button import Button
from programming_concepts.three_card_monte.outcome_view import OutcomeView
from programming_concepts.three_card_monte.game_text import GameText

def main():

    #Create the game view window
    win = GraphWin("GameView", 700, 500)
    win.setBackground("lightblue")

    # creates three variables and starts them at zero.
    winCount = 0
    loseCount = 0
    choice = 0

    # draws the cards (buttons) and activates them.
    # card 1
    cb1 = Button(win, Point(175,175), 150, 250, "Option 1")
    cb1.activate()
    # card 2
    cb2 = Button(win, Point(350,175), 150, 250, "Option 2")
    cb2.activate()
    # card 3
    cb3 = Button(win, Point(525,175), 150, 250, "Option 3")
    cb3.activate()
    
    # Quit Button
    qb = Button(win, Point(350,450), 130, 45, "Quit")
    
    # Draws the visual representation of a correct choice or a wrong choice
    # The outcome is assigned to their respective cards
    outcome1 = OutcomeView(win, Point(175,175), 140)
    # Draws outcome 2
    outcome2 = OutcomeView(win, Point(350, 175), 140)
    # Draws outcome 3
    outcome3 = OutcomeView(win, Point(525, 175), 140)
    # Draws the game text
    message1 = GameText(win, Point(350, 10))
    
    

    # Creates a start point for the sentinel loop.
    correct = randrange(1,4)
    pt = win.getMouse()
    # Displays the welcome message. 
    message1.setValue(1)

    # Continues as long as the quit button isn't pressed.
    while not qb.clicked(pt):

        # Selects button 1 and checks if it is correct.
        if cb1.clicked(pt):
            choice = 1
            if choice == correct:
                winCount = winCount + 1
                # Displays the green circle and the win text for card 1.
                outcome1.setOutcome(1)
                message1.setValue(2)
                
            else:
                loseCount = loseCount + 1
                # Displays the red X and the lose text for card 1.
                outcome1.setOutcome(2)
                message1.setValue(3)
                
        # Event for Button 2
        elif cb2.clicked(pt):
            choice = 2
            # Second correct event
            if choice == correct:
                winCount = winCount + 1
                # Displays the green circle and the win text for card 2.
                outcome2.setOutcome(1)
                message1.setValue(2)
                
            else:
                loseCount = loseCount + 1
                # Displays the red X and the lose text for card 2.
                outcome2.setOutcome(2)
                message1.setValue(3)
                
        # Event for Button 3
        elif cb3.clicked(pt):
            choice = 3
            # Third correct event
            if choice == correct:
                winCount = winCount + 1
                # Displays the green circle and the win text for card 3.
                outcome3.setOutcome(1)
                message1.setValue(2)
                
            else:
                loseCount = loseCount + 1
                # Displays the red X and the lose text for card 3.
                outcome3.setOutcome(2)
                message1.setValue(3)
                
                
        # Resets loop, and random generator. 
        qb.activate()
        pt = win.getMouse()
        correct = randrange(1,4)
        # Resets outcome images.
        outcome1.setOutcome(0)
        outcome2.setOutcome(0)
        outcome3.setOutcome(0)

    # Converts win and lose count to strings.
    message1.setCount(winCount, loseCount)

    # Prints a message displaying wins and loses. 
    message1.setValue(4)
    win.getMouse()
    win.close()

main()
