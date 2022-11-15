import random


class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_black = max_block

    def block(self):
        random_value = random.randint(0, self.max_block)
