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
import time


def setup():
    places = []
    people = []
    monsters = []

    # create all the locations
    town = Location.Location("Greenbergg", 10, 500)
    cave = Location.Location("Kirsa Cava", 1, 0)
    market = Location.Location("Arda Del Bosques", 0.1, 1)

    places.extend([town, cave, market])

    # create all the people
    main_character = Entity.Entity("Odilie Fuchsg", "Human", True, 50)
    market_man = Entity.Entity("Irmalinda Garverg", "Human", True, 5000)

    people.extend([main_character, market_man])

    # create all the monsters
    dragon = Entity.Entity("Dragoness", "Dragon", False, 15)
    wizard = Entity.Entity("Kirsa Wizess", "Wizard", False, 15)
    goblin = Entity.Entity("Baldhild", "Goblin", False, 15)
    ogre = Entity.Entity("Ogrelad", "Ogre", False, 15)
    fairy = Entity.Entity("Faerie", "Fairy", True, 50)

    monsters.extend([dragon, wizard, goblin, ogre, fairy])

    # return the created objects (all in one line or else it breaks)
    return places, people, monsters


def menu():
    while True:
        print("*** Medieval Story World ***\n1. Go to Town\n2. Go to Market\n3. Go to Cave")
        try:
            menu_choice = int(input("> "))

            if menu_choice == 1:
                pass
            elif menu_choice == 2:
                pass
            elif menu_choice == 3:
                pass
            else:
                print("You entered an invalid integer. Please try again")
                continue
        except ValueError:
            # Handle the case when the user enters a non-integer value
            print("Please enter a valid integer.")
            continue
        break

def get_main_character(people):
    for person in people:
        if person.name == "Odilie Fuchsg":
            return person


def fight(people, monsters):
    # get the main character
    me = get_main_character(people)

    if me.get_health() <= 0:
        print("You don't have any health! You have died. Goodbye!")
    else:
        # get the random monster to fight
        rand_index = random.randint(0, len(monsters) - 1)
        monster = monsters[rand_index]

        if not monster.get_good():
            print(f"Fighting {monster.get_name()}, a {monster.get_species()}!")

            while me.get_health() > 0 and monster.get_health() > 0:
                print(f"You have {me.get_health()} health and {monster.get_name()} has {monster.get_health()} health.")
                monster_health_before_attack = monster.get_health()

                # Player's attack
                monster = monster.set_fighting_health(monster.get_health() - me.get_strength())
                time.sleep(2)
                print(f"You struck the {monster.get_name()} with a strength of {me.get_strength()}.")
                print(f"{monster.get_name()} now has a health of {monster.get_health()} and you have a health of {me.get_health()}.")

                # Check if monster is defeated
                if monster.get_health() <= 0:
                    print(f"You defeated {monster.get_name()}! You have now won {monster.get_gold()} gold.")
                    me.set_gold(me.get_gold() + monster.get_gold())
                    monsters.pop(rand_index)
                    menu()
                    break  # Exit the loop if the monster is defeated

                # Monster's attack
                me = me.set_fighting_health(me.get_health() - monster.get_strength())
                time.sleep(2)
                print(f"{monster.get_name()} struck you with a strength of {monster.get_strength()}.")
                print(f"You now have a health of {me.get_health()} and {monster.get_name()} has a health of {monster.get_health()}.")

                # Check if the player is defeated
                if me.get_health() <= 0:
                    print(f"You died fighting the {monster.get_name()}. Goodbye!")
                    break  # Exit the loop if the player is defeated

            # Remove the defeated monster from the list after the fight is over
            monsters.pop(rand_index)
            menu()
        else:
            print(f"You have stumbled upon a magical {monster.get_species()}. These creatures are good!")
            print(f"Fairy: My name is {monster.get_name()}. It is so wonderful to meet you, {me.get_name()}!")
            print(f"If you are able to answer this challenging riddle, I will give you 25 gold!\nReady?")
            time.sleep(2)
            print("What can you break, even if you never pick it up or touch it? ")
            answer_one = input("> ").lower()
            if answer_one == "a promise" or answer_one == "promise" or answer_one == "promises":
                print("You did it! A promise can be broken without being touched! You have won 25 gold! However,"
                      "would you like a chance to double your gold...?\nIf you get this next riddle right, you win "
                      "50 gold instead! But if you answer incorrectly, you win nothing.")
                play_again = input("So, what do you say (y/n): ").lower()
                if play_again == "yes" or play_again == "y":
                    print("Wonderful choice! Get ready for the most challenging question of your life...")
                    time.sleep(2)
                    print("I have branches, but no fruit, trunk or leaves. What am I?")
                    answer_two = input("> ").lower()
                    if answer_two == "bank" or answer_two == "banks" or answer_two == "a bank":
                        print("Congratulations! Banks was the right answer! Here is your 50 gold as promised...")
                        time.sleep(2)
                        me.set_gold(me.get_gold() + 50)
                        print(f"You now have {me.get_gold()} gold.\n")
                        monsters.pop(rand_index)
                        menu()
                    else:
                        print("I'm sorry, the correct answer was 'bank.' Better luck next time. As a result of losing"
                              "this question, you don't win any gold...\n")
                        monsters.pop(rand_index)
                        menu()
                elif play_again == "no" or "n":
                    print("Playing it safe I see, wise of you. Here's your 25 gold as promised...")
                    time.sleep(2)
                    me.set_gold(me.get_gold() + 25)
                    print(f"You now have {me.get_gold()} gold.")
                    monsters.pop(rand_index)
                    menu()
                else:
                    print("That wasn't a valid response. You just lost all of your gold!")
                    me.set_gold(0)
                    print(f"You now have {me.get_gold()} gold.")
                    monsters.pop(rand_index)
                    menu()
            else:
                print("I'm sorry, the correct answer was 'a promise.' You don't win this time, but here's an extra"
                      " 5 gold just for playing along :)")
                time.sleep(2)
                me.set_gold(me.get_gold() + 5)
                print(f"You now have {me.get_gold()} gold.\n")
                monsters.pop(rand_index)
                menu()


def main():
    places, people, monsters = setup()
    fight(people, monsters)


if __name__ == '__main__':
    main()
