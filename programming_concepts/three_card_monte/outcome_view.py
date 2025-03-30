from programming_concepts.classes.graphics import *


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
