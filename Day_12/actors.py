import random

class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def defensive_role(self):
        roll = random.randint(1,12)
        return roll * self.level

class Dragon(Creature):
    def __init__(self, name, level, scaliness, breaths_fire):
        super().__init__(name, level)
        self.scaliness = scaliness
        self.breaths_fire = breaths_fire

    def defensive_role(self):
        roll = super().defensive_role()
        value = roll * self.scaliness
        if self.breaths_fire:
            value = value * 2

        return value

class Wizard(Creature):

    def attack(self, creature):
        my_roll = self.defensive_role()
        their_roll = creature.defensive_role()

        print("my_roll {}   their_roll {}".format(my_roll, their_roll))

        return my_roll >= their_roll


    