# dice.py

from random import randrange

from programming_concepts.classes.graphics import Circle, Point, Rectangle


class Dice:
    def __init__(self):
        self.dice = [0] * 5
        self.roll_all()

    def roll(self, which):
        for pos in which:
            self.dice[pos] = randrange(1, 7)

    def roll_all(self):
        self.roll(range(5))

    def values(self):
        return self.dice[:]

    def score(self):
        # Create the counts list
        counts = [0] * 7
        for value in self.dice:
            counts[value] = counts[value] + 1

        # score the hand
        if 5 in counts:
            return "Five of a Kind", 30
        elif 4 in counts:
            return "Four of a Kind", 15
        elif (3 in counts) and (2 in counts):
            return "Full House", 12
        elif 3 in counts:
            return "Three of a Kind", 8
        elif not (2 in counts) and (counts[1] == 0 or counts[6] == 0):
            return "Straight", 20
        elif counts.count(2) == 2:
            return "Two Pairs", 5
        else:
            return "Garbage", 0


class DieView:
    """DieView is a widget that displays a graphical
    representation of a standard six-sided die."""

    def __init__(self, win, center, size):
        """Create a view of a die, e.g.:
           d1 = GDie(myWin, Point(40,50), 20)
        creates a die centered at (40,50) having sides
        of length 20."""

        # first define some standard values
        self.win = win
        self.background = "white"  # color of die face
        self.foreground = "black"  # color of the pips
        self.psize = 0.1 * size  # radius of each pip
        hsize = size / 2.0  # half of size
        offset = 0.6 * hsize  # distance from center to outer pips

        # create a square for the face
        cx, cy = center.getX(), center.getY()
        p1 = Point(cx - hsize, cy - hsize)
        p2 = Point(cx + hsize, cy + hsize)
        rect = Rectangle(p1, p2)
        rect.draw(win)
        rect.setFill(self.background)

        # Create 7 circles for standard pip locations
        self.pips = [
            self.__make_pip(cx - offset, cy - offset),
            self.__make_pip(cx - offset, cy),
            self.__make_pip(cx - offset, cy + offset),
            self.__make_pip(cx, cy),
            self.__make_pip(cx + offset, cy - offset),
            self.__make_pip(cx + offset, cy),
            self.__make_pip(cx + offset, cy + offset),
        ]

        # Create a table for which pips are on for each value
        self.onTable = [
            [],
            [3],
            [2, 4],
            [2, 3, 4],
            [0, 2, 4, 6],
            [0, 2, 3, 4, 6],
            [0, 1, 2, 4, 5, 6],
        ]

        self.set_value(1)

    def __make_pip(self, x, y):
        """Internal helper method to draw a pip at (x,y)"""
        pip = Circle(Point(x, y), self.psize)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        return pip

    def set_value(self, value):
        """Set this die to display value."""
        # Turn all the pips off
        for pip in self.pips:
            pip.setFill(self.background)

        # Turn the appropriate pips back on
        for i in self.onTable[value]:
            self.pips[i].setFill(self.foreground)


class ColorDieView(DieView):
    """
    Implementation of a DieView with changeable forground color, illustrates inheritance.
    """

    def set_value(self, value):
        self.value = value  # remember this value
        DieView.set_value(self, value)  # call setValue from parent class

    def set_color(self, color):
        self.foreground = color
        self.set_value(self.value)


class MSDie:

    def __init__(self, sides):
        self.sides = sides
        self.value = 1

    def roll(self):
        self.value = randrange(1, self.sides + 1)

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value
