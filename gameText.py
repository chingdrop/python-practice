# gameText.py
from graphics import *
class GameText:
    """ A custom wigdet that displays text. The text can be changed by its value.
        The text will isplay the win, lose, welcoome and quit messages."""
    
    def __init__(self, win, center):
        """Creates Interactive Text, e.g.:
           message = GameText(myWin, Point(40,50))
        creates interactive text centered at (40,50)"""

        # initializes are parameters used by the methods.
        self.win = win            
        cx, cy = center.getX(), center.getY()
        self.welcome = "Welcome to Three Card Monte"
        self.winMessage = "You win! Try again or quit."
        self.loseMessage = "You lose! Try again or quit."
        self.w = "0"
        self.l = "0"

        # Constructs interactive text. 
        self.Message1 = self.__makeText(cx, cy)

    def __makeText(self, x, y):
        "helper method that creates the interactive text."
        gameMessage = Text(Point(x,y), "")
        gameMessage.setText("Welcome to Three Card Monte")
        gameMessage.draw(self.win)
        gameMessage.setTextColor("white")
        return gameMessage

    def setCount(self, winCount, loseCount):
        "A mutator method that updates the win/lose method."
        self.w = str(winCount)
        self.l = str(loseCount)

    def setValue(self, value):
        "Sets the value that indicates which message to display."
        # default value
        self.Message1.setText("")

        # changes game text based on the outcome of the game.
        if value == 1:
            self.Message1.setText(self.welcome)
        elif value == 2:
            self.Message1.setText(self.winMessage)
        elif value == 3:
            self.Message1.setText(self.loseMessage)

        # Puts together the quit message.
        else:
            self.Message1.setText("You won "+self.w+" times and lost "+self.l+" times. Click anywhere to close.")
