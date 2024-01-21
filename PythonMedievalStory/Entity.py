import random


class Entity:
    name = ""
    species = ""
    good = True
    health = 0
    strength = 0
    gold = 0

    def __init__(self, name, species, good, gold):
        self.set_name(name)
        self.set_species(species)
        self.set_good(good)
        self.set_health()
        self.set_strength()
        self.set_gold(gold)

    def roll_dice(self):
        die_1 = random.randint(1, 6)
        die_2 = random.randint(1, 6)
        return die_1 * die_2

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_species(self, species):
        self.species = species

    def get_species(self):
        return self.species

    def set_good(self, good):
        self.good = good

    def get_good(self):
        return self.good

    def set_health(self):
        self.health = self.roll_dice()

    def set_fighting_health(self, health):
        self.health = health
        return self

    def get_health(self):
        return self.health

    def set_strength(self):
        self.strength = self.roll_dice()

    def get_strength(self):
        return self.strength

    def set_gold(self, gold):
        self.gold = gold

    def get_gold(self):
        return self.gold
