# File - pokerapp.py
# Latest Version - Chapter 12

from programming_concepts.classes.dice import Dice


class PokerApp:

    def __init__(self, interface):
        self.dice = Dice()
        self.money = 100
        self.interface = interface

    def run(self):
        while self.money >= 10 and self.interface.want_to_play():
            self.play_round()
        self.interface.close()

    def play_round(self):
        self.money = self.money - 10
        self.interface.set_money(self.money)
        self.do_rolls()
        result, score = self.dice.score()
        self.interface.show_result(result, score)
        self.money = self.money + score
        self.interface.set_money(self.money)

    def do_rolls(self):
        self.dice.roll_all()
        roll = 1
        self.interface.set_dice(self.dice.values())
        toRoll = self.interface.choose_dice()
        while roll < 3 and toRoll != []:
            self.dice.roll(toRoll)
            roll = roll + 1
            self.interface.set_dice(self.dice.values())
            if roll < 3:
                toRoll = self.interface.choose_dice()
