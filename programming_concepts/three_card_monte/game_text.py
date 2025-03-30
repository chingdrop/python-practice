from programming_concepts.classes.graphics import *


class GameText:
    """A custom wigdet that displays text. The text can be changed by its value.
    The text will isplay the win, lose, welcoome and quit messages."""

    def __init__(self, win, center):
        """Creates Interactive Text, e.g.:
           message = GameText(myWin, Point(40,50))
        creates interactive text centered at (40,50)"""

        # initializes are parameters used by the methods.
        self.win = win
        cx, cy = center.getX(), center.getY()
        self.welcome = "Welcome to Three Card Monte"
        self.win_message = "You win! Try again or quit."
        self.lose_message = "You lose! Try again or quit."
        self.w = "0"
        self.l = "0"

        # Constructs interactive text.
        self.message1 = self.__make_text(cx, cy)

    def __make_text(self, x, y):
        "helper method that creates the interactive text."
        game_message = Text(Point(x, y), "")
        game_message.setText("Welcome to Three Card Monte")
        game_message.draw(self.win)
        return game_message

    def set_count(self, win_count, lose_count):
        "A mutator method that updates the win/lose method."
        self.w = str(win_count)
        self.l = str(lose_count)

    def set_value(self, value):
        "Sets the value that indicates which message to display."
        # default value
        self.message1.setText("")

        # changes game text based on the outcome of the game.
        if value == 1:
            self.message1.setText(self.welcome)
        elif value == 2:
            self.message1.setText(self.win_message)
        elif value == 3:
            self.message1.setText(self.lose_message)

        # Puts together the quit message.
        else:
            self.Message1.setText(
                "You won "
                + self.w
                + " times and lost "
                + self.l
                + " times. Click anywhere to close."
            )
