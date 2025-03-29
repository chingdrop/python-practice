# File - rball.py
# Latest Version - Chapter 9
# Simulation of a racquetball game

from random import random


def main():
    print_intro()
    prob_a, prob_b, n = get_inputs()
    wins_a, wins_b = sim_n_games(n, prob_a, prob_b)
    print_summary(wins_a, wins_b)


def print_intro():
    print(
        "This program simulates a game of racquet ball between two players called A and B."
    )
    print(
        "The abilities of each player is indicated by a probability (a number between 0 and 1) that the player wins the point when serving."
    )
    print("Player A always has the first serve.")


def get_inputs():
    # Returns the three simulation parameters
    a = float(input("What is the prob. player A wins a serve? "))
    b = float(input("What is the prob. player B wins a serve? "))
    n = int(input("How many games to simulate? "))
    return a, b, n


def sim_n_games(n, prob_a, prob_b):
    # Simulates n games of racquetball between players whosevabilities are represented by the probability of winning a serve.
    # Returns number of wins for A and B
    wins_a = wins_b = 0
    for i in range(n):
        score_a, score_b = sim_one_game(prob_a, prob_b)
        if score_a > score_b:
            wins_a = wins_a + 1
        else:
            wins_b = wins_b + 1
    return wins_a, wins_b


def sim_one_game(prob_a, prob_b):
    # Simulates a single game or racquetball between players whose abilities are represented by the probability of winning a serve.
    # Returns final scores for A and B
    serving = "A"
    score_a = 0
    score_b = 0
    while not game_over(score_a, score_b):
        if serving == "A":
            if random() < prob_a:
                score_a = score_a + 1
            else:
                serving = "B"
        else:
            if random() < prob_b:
                score_b = score_b + 1
            else:
                serving = "A"
    return score_a, score_b


def game_over(a, b):
    # a and b represent scores for a racquetball game
    # Returns True if the game is over, False otherwise.
    return a == 15 or b == 15


def print_summary(wins_a, wins_b):
    # Prints a summary of wins for each player.
    n = wins_a + wins_b
    print(f"\nGames simulated: {n}")
    print(f"Wins for A: {wins_a} ({wins_a / n:0.1%})")
    print(f"Wins for A: {wins_b} ({wins_b / n:0.1%})")


if __name__ == "__main__":
    main()
