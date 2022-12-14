import random
from ability import Ability
from armor import Armor
from weapon import Weapon
import time


class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.abilities = list()
        self.armors = list()
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def defend(self):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block

    def take_damage(self, damage):
        block = self.defend()
        damage = damage - block
        if block < 0:
            return
        self.current_health -= damage

    def is_alive(self):
        if self.current_health <= 0:
            return False
        else:
            return True

    def fight(self, opponent):
        """
        Current Hero will take turns fighting the opponent hero passed in.
        """
        winner = False
        while winner == False:
            if len(self.abilities) == 0 and len(opponent.abilities) == 0:
                print("Draw")
                winner = "Draw"
            while self.current_health > 0 and opponent.current_health > 0:
                print("Begin battle: ")
                print(f"Hero current health: {self.current_health}")
                print(f"Opponent current health: {opponent.current_health}")
                opponent.take_damage(self.attack())
                self.take_damage(opponent.attack())
                print(f"Hero new health: {self.current_health}")
                print(f"Opponent new health: {opponent.current_health}")
                time.sleep(5)
            if opponent.is_alive() == False:
                self.add_kill(1)
                opponent.add_death(1)
                winner = self.name
            if self.is_alive() == False:
                self.add_death(1)
                opponent.add_kill(1)
                winner = opponent.name

        print(f"{winner} won!")

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_death(self, num_deaths):
        self.deaths += num_deaths


if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    hero2 = Hero("Andrew")
    weapon = Weapon("Lasso of Truth", 90)
    armor = Armor("Shield", 200)
    hero.add_armor(armor)
    hero.add_weapon(weapon)
    hero2.add_weapon(weapon)
    hero2.add_armor(armor)

    hero.fight(hero2)
