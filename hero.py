import random
from ability import Ability
from armor import Armor


class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.abilities = list()
        self.armors = list()
        self.current_health = starting_health

    def add_ability(self, ability):
        self.abilities.append(ability)

    def attack():
        pass

    def defend(incoming_damage):
        pass

    def take_damage(self, damage):
        pass

    def is_alive():
        pass

    def fight(self, opponent):
        """
        Current Hero will take turns fighhting the opponent hero passed in.
        """
        fighters = [self, opponent]
        winner = random.choice(fighters)
        fighters.remove(winner)
        loser = fighters[0]

        print(f"{winner.name} defeats {loser.name}!")


if __name__ == "__main__":
    ability = Ability("Great Debugging", 50)
    ability2 = Ability("Hydro Pump", 100)
    hero = Hero("Grace Hopper", 200)
    hero.add_ability(ability)
    hero.add_ability(ability2)
    print(hero.abilities)
