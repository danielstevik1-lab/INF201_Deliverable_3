from dice import Dice

class Weapon:
    """Represents a weapon in the game"""


    def __init__(self, name:str, damage_dice: Dice)->None:
        """Initialize weapon"""
        self.name = name
        self.damage_dice = damage_dice


    def roll_damage(self) ->int:
        """Dice that rolls damage points given to target"""
        return self.damage_dice()


    def __repr__(self) -> None:
        """Representation of weapon object"""
        return f"Weapon(name = '{self.name}', damage_dice = {self.damage_dice})"


    def __str__(self) -> None:
        """String representation of weapon object"""
        return f"Weapon: {self.name}, (Dice: {self.damage_dice})"
    

