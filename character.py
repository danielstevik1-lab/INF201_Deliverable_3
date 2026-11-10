""" ----- Task 1 ----- Character class ----- """

from items import Weapon

class character:
    "Represents a character in a game"

    def __init__(self, name:str, hp_max: int = 100, damage: int = 10, weapon: Weapon = None)->None:
        """
        Initialize character:
            
        Args:
            name(str):      The name of the character
            hp_max(int):    Max HitPoints, default = 100
            damage(int):    Damage delt when a character attacks, default = 10
        """
        self.name = name
        self.hp_max = hp_max
        self.damage = damage
        self._hp = hp_max
        self.weapon = weapon


    def take_damage(self, amount: int) -> None:
        """Reduces the characters HP without going below 0"""
        self._hp = max(self._hp -amount, 0)


    def heal(self, amount:int) -> None:
        """Increases character health by amount withouth exceeding max health"""
        self._hp = min(self._hp + amount, self.hp_max)


    def attack(self, target) -> None:
        """Attack and deal damage to target character"""
        if self.weapon is not None:
            inflicted_damage = self.weapon.roll_damage()
        else:
            inflicted_damage = self.damage
        target.take_damage(inflicted_damage)

    def introduce(self)->None:
        """Creates string that introduces character"""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of character objects"""
        return f"<Character name ={self.name} , hp = {self.hp}, damage ={self.damage}, weapon ={self.weapon}>"
    def __str__(self) -> str:
        """String representation of character object"""
        weapon_str = f" with {self.weapon}" if self.weapon else ""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage {weapon_str}"

    @property
    def hp(self)-> int:
        """Public read-only  property to inspect HP without allowing direct, unsafe edits."""
        return self._hp

    @property
    def is_alive(self)->bool:
        """Public read-only property returning True if character is alive, else false """
        return self._hp > 0


