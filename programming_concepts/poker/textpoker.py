# File - textpoker.py
# Latest Version - Chapter 12

from programming_concepts.poker.pokerapp import PokerApp


class TextInterface:

    def __init__(self):
        print("Welcome to video poker.")

    def set_money(self, amt):
        print(f"You currently have ${amt}.")

    def set_dice(self, values):
        print("Dice:", values)

    def want_to_play(self):
        ans = input("Do you wish to try your luck? ")
        return ans[0] in "yY"

    def close(self):
        print("\nThanks for playing!")

    def show_result(self, msg, score):
        print(f"{msg}. You win ${score}.")

    def choose_dice(self):
        return eval(input("Enter list of which to change ([] to stop) "))


inter = TextInterface()
app = PokerApp(inter)
app.run()
