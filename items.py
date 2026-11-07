from dice import Dice

class Weapon:
    """Represents a weapon in the game"""


    def __init__(self, name:str, damage_dice: Dice):
        """Initialize weapon"""
        self.name = name
        self.damage_dice = damage_dice


    def roll_damage(self):
        






