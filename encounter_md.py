import random
from constant_md import STARS


class EncounterCls:
    def __init__(self, game):
        self.game = game
        self.pirate_risk = 25
        self.pirate_strength = 10
        self.chance_for_escape = 33
        self.check_for_pirate_fn()

    def check_for_pirate_fn(self):
        rusalt = random.randint(0, 100)
        if rusalt <= self.pirate_risk:
            self.pirate_attack_fn()

    def pirate_attack_fn(self):
        print(STARS)
        print("PIRATES!!!")
        print(STARS)
        self.number_of_pireats = random.randint(1, self.pirate_strength)
        fight_priates = True
        while fight_priates:
            print("There are %s priates remaining" % self.number_of_pireats)
            print("You have %s cannons and your ship health is %s" % (self.game.cannons, self.game.ship_health))
            print("")
            attack_inp = input("What do you wish to do? R)un or F)ight")
            if attack_inp == "r":
                if self.run_fn():
                    fight_priates = False
            if attack_inp == "f":
                self.fight_fn()

    def run_fn(self):
        print("You try to run")
        rusalt = random.randint(0, 100)
        if rusalt <= self.chance_for_escape:
            print("You escaped!")
            return True
        else:
            print("You did't get away!")
            return False

    def fight_fn(self):
        pass
