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

    def add_armor(self, armor):
        self.armors.append(armor)

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
        # FIX IF BLOCK IS LARGER THAN DAMAGE
        self.current_health -= damage

    def is_alive(self):
        if self.current_health <= 0:
            return False
        else:
            return True

    def fight(self, opponent):
        """
        Current Hero will take turns fighhting the opponent hero passed in.
        """
        winner = False
        while winner == False:
            if len(self.abilities) == 0 and len(opponent.abilties) == 0:
                print("Draw")
                winner == "Draw"
            opponent.take_damage(self.attack())
            self.take_damage(opponent.attack())
            if opponent.is_alive() == False:
                winner = self.name
            if self.is_alive() == False:
                winner = opponent.name

        print(f"{winner} won!")

        # MUST FIX EDGE CASES


if __name__ == "__main__":
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
