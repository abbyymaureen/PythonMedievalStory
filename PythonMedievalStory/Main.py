"""
@author abby_brown
@filename Main.py
@date 01/18/24

This program allows the user to play a console-based medieval times game. The user will be able
to travel around the medieval world, kill magical creatures, and make friends along the way.
"""
import Location
import Entity
import random


def setup():
    places = []
    people = []
    monsters = []

    # Instantiate Location and Entity objects
    locations = Location()
    entities = Entity()

    # create all the locations
    town = locations("Greenbergg", 10, 500)
    cave = locations("Kirsa Cava", 1, 0)
    market = locations("Arda Del Bosques", 0.1, 1)

    places.extend([town, cave, market])

    # create all the people
    main_character = entities("Odilie Fuchsg", "Human", True, 50)
    market_man = entities("Irmalinda Garverg", "Human", True, 5000)

    people.extend([main_character, market_man])

    # create all the monsters
    dragon = entities("Dragoness", "Dragon", False, 15)
    wizard = entities("Kirsa Wizess", "Wizard", False, 15)
    goblin = entities("Baldhild", "Goblin", False, 15)
    ogre = entities("Ogrelad", "Ogre", False, 15)
    fairy = entities("Faerie", "Fairy", True, 50)

    monsters.extend([dragon, wizard, goblin, ogre, fairy])

    # Return the created objects
    return places, people, monsters


def get_main_character(people):
    for person in people:
        if person.name == "Odilie Fuchsg":
            return person


def fight(places, people, monsters):
    # get the main character
    me = get_main_character(people)

    # get the random monster to fight
    rand_index = random.randint(0, len(monsters) - 1)
    monster = monsters[rand_index]




def main():
    places, people, monsters = setup()
    fight(places, people, monsters)


if __name__ == '__main__':
    main()
