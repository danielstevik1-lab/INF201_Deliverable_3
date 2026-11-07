class character:
    "Represents a character in a game"

    def __init__(self, name:str, hp_max: int = 100, damage: int = 10):
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

    def attack(self, target) -> None:
        """Attack and deal damage to target character"""
        target._hp -= self.damage
        target._hp = max(target._hp, 0)     #Target hp cannot end up lower than 0.

    def introduce(self)->None:
        """Creates string that introduces character"""
    print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of character objects"""
        return f"<Character name ={self.name} , hp = {self.hp}, damage ={self.damage}>"
    def __str__(self) -> str:
        """String representation of character object"""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"

    @property
    def hp(self)-> int:
        """Public read-only  property to inspect HP without allowing direct, unsafe edits."""
        return self._hp



