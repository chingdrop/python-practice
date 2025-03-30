# Craig Hurely
# 2017/11/02
# threecardmonte.py

from random import randrange
from src.classes.graphics import Circle, GraphWin, Line, Point, Text
from src.classes.button import Button

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
            self.message1.setText(
                f"You won {self.w} times and lost {self.l} times. Click anywhere to close."
            )


class OutcomeView:
    """Outcome View is a widget that creates a
    visual interpretation of a win and a lose."""

    def __init__(self, win, center, size):
        """Create a circle for win or an X for lose, e.g.:
           outcome1 = OutcomeView(myWin, Point(40,50), 20)
        creates a circle and an ex centered at (40, 50)
        and with the size of 20."""

        # Constructs the parameters: colors, dimensions.
        self.win = win
        self.background = "peachpuff"
        self.correct = "green"
        self.wrong = "red"
        cx, cy = center.getX(), center.getY()
        self.csize = size / 2.5
        lsize = size / 2.0

        # Create the correct or wrong symbols for the outcome of the game
        self.correct1 = self.__make_correct(cx, cy)
        self.wrong1 = self.__make_wrong(cx - lsize, cx + lsize, cy + lsize, cy - lsize)
        self.wrong2 = self.__make_wrong(cx + lsize, cx - lsize, cy + lsize, cy - lsize)

    def __make_correct(self, x, y):
        "Creates a circle and sets the background to the same color as the card."
        correct_outcome = Circle(Point(x, y), self.csize)
        correct_outcome.setFill(self.background)
        correct_outcome.setOutline(self.background)
        correct_outcome.draw(self.win)
        return correct_outcome

    def __make_wrong(self, x1, x2, y1, y2):
        "Creates an X and sets the background to the card."
        p1 = Point(x1, y1)
        p2 = Point(x2, y2)
        wrong_outcome = Line(p1, p2)
        wrong_outcome.draw(self.win)
        wrong_outcome.setFill(self.background)
        return wrong_outcome

    def set_outcome(self, value):
        "Set the value of the image to color in a green circle or a red X"
        # defaults the images to the card color.
        self.correct1.setFill(self.background)
        self.wrong1.setFill(self.background)
        self.wrong2.setFill(self.background)

        # changes the image to the correct color.
        if value == 1:
            self.correct1.setFill(self.correct)
        elif value == 2:
            self.wrong1.setFill(self.wrong)
            self.wrong2.setFill(self.wrong)
        else:
            self.correct1.setFill(self.background)
            self.wrong1.setFill(self.background)
            self.wrong2.setFill(self.background)


def three_card_monte():

    # Create the game view window
    win = GraphWin("GameView", 700, 500)
    win.setBackground("lightblue")

    # creates three variables and starts them at zero.
    win_count = 0
    lose_count = 0
    choice = 0

    # draws the cards (buttons) and activates them.
    # card 1
    cb1 = Button(win, Point(175, 175), 150, 250, "Option 1")
    cb1.activate()
    # card 2
    cb2 = Button(win, Point(350, 175), 150, 250, "Option 2")
    cb2.activate()
    # card 3
    cb3 = Button(win, Point(525, 175), 150, 250, "Option 3")
    cb3.activate()

    # Quit Button
    qb = Button(win, Point(350, 450), 130, 45, "Quit")

    # Draws the visual representation of a correct choice or a wrong choice
    # The outcome is assigned to their respective cards
    outcome1 = OutcomeView(win, Point(175, 175), 140)
    # Draws outcome 2
    outcome2 = OutcomeView(win, Point(350, 175), 140)
    # Draws outcome 3
    outcome3 = OutcomeView(win, Point(525, 175), 140)
    # Draws the game text
    message1 = GameText(win, Point(350, 10))

    # Creates a start point for the sentinel loop.
    correct = randrange(1, 4)
    pt = win.getMouse()
    # Displays the welcome message.
    message1.set_value(1)

    # Continues as long as the quit button isn't pressed.
    while not qb.clicked(pt):

        # Selects button 1 and checks if it is correct.
        if cb1.clicked(pt):
            choice = 1
            if choice == correct:
                win_count = win_count + 1
                # Displays the green circle and the win text for card 1.
                outcome1.set_outcome(1)
                message1.set_value(2)

            else:
                lose_count = lose_count + 1
                # Displays the red X and the lose text for card 1.
                outcome1.set_outcome(2)
                message1.set_value(3)

        # Event for Button 2
        elif cb2.clicked(pt):
            choice = 2
            # Second correct event
            if choice == correct:
                win_count = win_count + 1
                # Displays the green circle and the win text for card 2.
                outcome2.set_outcome(1)
                message1.set_value(2)

            else:
                lose_count = lose_count + 1
                # Displays the red X and the lose text for card 2.
                outcome2.set_outcome(2)
                message1.set_value(3)

        # Event for Button 3
        elif cb3.clicked(pt):
            choice = 3
            # Third correct event
            if choice == correct:
                win_count = win_count + 1
                # Displays the green circle and the win text for card 3.
                outcome3.set_outcome(1)
                message1.set_value(2)

            else:
                lose_count = lose_count + 1
                # Displays the red X and the lose text for card 3.
                outcome3.set_outcome(2)
                message1.set_value(3)

        # Resets loop, and random generator.
        qb.activate()
        pt = win.getMouse()
        correct = randrange(1, 4)
        # Resets outcome images.
        outcome1.set_outcome(0)
        outcome2.set_outcome(0)
        outcome3.set_outcome(0)

    # Converts win and lose count to strings.
    message1.set_count(win_count, lose_count)

    # Prints a message displaying wins and loses.
    message1.set_value(4)
    win.getMouse()
    win.close()
