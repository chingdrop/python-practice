# File - oop_rball.py
# Latest Version - Chapter 12
# Simulation of a racquet game. Illustrates design with objects.

from random import random


class Player:
    # A Player keeps track of service probability and score

    def __init__(self, prob):
        # Create a player with this probability
        self.prob = prob
        self.score = 0

    def wins_serve(self):
        # Returns a Boolean that is true with probability self.prob
        return random() <= self.prob

    def inc_score(self):
        # Add a point to this player's score
        self.score = self.score + 1

    def get_score(self):
        # Returns this player's current score
        return self.score


class RBallGame:
    # A RBallGame represents a game in progress. A game has two players
    # and keeps track of which one is currently serving.

    def __init__(self, prob_a, prob_b):
        # Create a new game having players with the given probs.
        self.player_a = Player(prob_a)
        self.player_b = Player(prob_b)
        self.server = self.player_a  # Player A always serves first

    def play(self):
        # Play the game to completion
        while not self.is_over():
            if self.server.wins_serve():
                self.server.inc_score()
            else:
                self.change_server()

    def is_over(self):
        # Returns game is finished (i.e. one of the players has won).
        a, b = self.get_scores()
        return a == 15 or b == 15 or (a == 7 and b == 0) or (b == 7 and a == 0)

    def change_server(self):
        # Switch which player is serving
        if self.server == self.player_a:
            self.server = self.player_b
        else:
            self.server = self.player_a

    def get_scores(self):
        # Returns the current scores of player A and player B
        return self.player_a.get_score(), self.player_b.get_score()


class SimStats:
    # SimStats handles accumulation of statistics across multiple
    #   (completed) games. This version tracks the wins and shutouts for
    #   each player.

    def __init__(self):
        # Create a new accumulator for a series of games
        self.wins_a = 0
        self.wins_b = 0
        self.shuts_a = 0
        self.shuts_b = 0

    def update(self, game):
        # Determine the outcome of aGame and update statistics
        a, b = game.getScores()
        if a > b:  # A won the game
            self.wins_a = self.wins_a + 1
            if b == 0:
                self.shuts_a = self.shuts_a + 1
        else:  # B won the game
            self.wins_b = self.wins_b + 1
            if a == 0:
                self.shuts_b = self.shuts_b + 1

    def print_report(self):
        # Print a nicely formatted report
        n = self.wins_a + self.wins_b
        print("Summary of", n, "games:\n")
        print("          wins (% total)   shutouts (% wins)  ")
        print("--------------------------------------------")
        self.print_line("A", self.wins_a, self.shuts_a, n)
        self.print_line("B", self.wins_b, self.shuts_b, n)

    def print_line(self, label, wins, shuts, n):
        template = "Player {0}:{1:5}  ({2:5.1%}) {3:11}   ({4})"
        if wins == 0:  # Avoid division by zero!
            shutStr = "-----"
        else:
            shutStr = "{0:4.1%}".format(float(shuts) / wins)
        print(template.format(label, wins, float(wins) / n, shuts, shutStr))


def print_intro():
    print("This program simulates games of racquetball between two")
    print('players called "A" and "B".  The ability of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. Player A always")
    print("has the first serve.\n")


def get_inputs():
    # Returns the three simulation parameters
    a = float(input("What is the prob. player A wins a serve? "))
    b = float(input("What is the prob. player B wins a serve? "))
    n = int(input("How many games to simulate? "))
    return a, b, n


def oop_rball():
    print_intro()

    probA, probB, n = get_inputs()

    # Play the games
    stats = SimStats()
    for i in range(n):
        theGame = RBallGame(probA, probB)  # create a new game
        theGame.play()  # play it
        stats.update(theGame)  # extract info

    # Print the results
    stats.print_report()


oop_rball()
input("\nPress <Enter> to quit")
