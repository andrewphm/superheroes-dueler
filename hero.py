import random


class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def add_ability(self, ability):
        pass

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
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    hero1.fight(hero2)
