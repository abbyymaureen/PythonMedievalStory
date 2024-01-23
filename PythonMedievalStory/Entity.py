"""
@author abbybrown
@date 01/20/24
@filename Entity.py

The entity class allows for the generation of people and monsters.
"""
import random


class Entity:
    name = ""
    species = ""
    good = True
    health = 0
    strength = 0
    gold = 0

    # constructor
    def __init__(self, name, species, good, gold):
        self.set_name(name)
        self.set_species(species)
        self.set_good(good)
        self.set_health()
        self.set_strength()
        self.set_gold(gold)

    # roll dice function - returns product of two random dice rolls
    def roll_dice(self):
        die_1 = random.randint(1, 6)
        die_2 = random.randint(1, 6)
        return die_1 * die_2

    # sets the name of the entity
    def set_name(self, name):
        self.name = name

    # gets the name of the entity
    def get_name(self):
        return self.name

    # sets the species of the entity
    def set_species(self, species):
        self.species = species

    # gets the species of the entity
    def get_species(self):
        return self.species

    # sets true if an entity is a 'good' guy or false if not
    def set_good(self, good):
        self.good = good

    # gets whether the entity is good (true) or bad (false)
    def get_good(self):
        return self.good

    # sets the health of the entity using the roll dice function (random per entity)
    def set_health(self):
        self.health = self.roll_dice()

    # allows for setting the health of the entity
    def set_fighting_health(self, health):
        self.health = health
        return self

    # gets the health of the entity
    def get_health(self):
        return self.health

    # sets the strength of the entity using the roll dice function (random per entity)
    def set_strength(self):
        self.strength = self.roll_dice()

    # allows for setting the strength of the entity
    def set_fighting_strength(self, strength):
        self.strength = strength
        return self

    # gets the strength of the entity
    def get_strength(self):
        return self.strength

    # sets the gold the entity has
    def set_gold(self, gold):
        self.gold = gold

    # gets the gold the entity has
    def get_gold(self):
        return self.gold
