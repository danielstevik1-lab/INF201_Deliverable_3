""" ----- Task 1 og Task 4 ----- Character class og Specializations ----- """

from items import Weapon

class Character:
    """Represents a character in a game"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, weapon: Weapon = None) -> None:
        """
        Initialize character:
        Args:
            name (str): The name of the character
            hp_max (int): Max HitPoints, default = 100
            damage (int): Damage dealt when a character attacks, default = 10
            weapon (Weapon): Optional weapon equipped by character
        """
        self.name = name
        self.hp_max = hp_max
        self.damage = damage
        self._hp = hp_max  # Beskyttet attributt for HP[cite: 2, 4]
        self.weapon = weapon

    # --- TASK 1 METODER ---
    def take_damage(self, amount: int) -> None:
        """Reduces the characters HP without going below 0"""
        self._hp = max(self._hp - amount, 0)

    def heal(self, amount: int) -> None:
        """Increases character health by amount without exceeding max health"""
        self._hp = min(self._hp + amount, self.hp_max)

    def attack(self, target) -> None:
        """Attack and deal damage to target character using weapon or base damage[cite: 2, 3]"""
        if self.weapon is not None:
            inflicted_damage = self.weapon.roll_damage()
        else:
            inflicted_damage = self.damage
        target.take_damage(inflicted_damage)

    def introduce(self) -> None:
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        return f"<Character name={self.name}, hp={self.hp}, damage={self.damage}, weapon={self.weapon}>"

    def __str__(self) -> str:
        weapon_str = f" with {self.weapon}" if self.weapon else ""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage {weapon_str}"

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits[cite: 4]."""
        return self._hp

    @property
    def is_alive(self) -> bool:
        """Public read-only property returning True if character is alive, else false"""
        return self._hp > 0


# --- TASK 4 SUBKLASSER (SPESIALISERINGER) ---

class Warrior(Character):
    """Represents a defensive specialist Warrior character"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, weapon: Weapon = None, armor: int = 5) -> None:
        super().__init__(name, hp_max, damage, weapon)
        self.armor = armor  #rustning med default verdi 5

    def take_damage(self, amount: int) -> None:
        """Reduces incoming damage by armor before applying it (minimum 0 damage)[cite: 3]"""
        reduced_damage = max(amount - self.armor, 0)
        super().take_damage(reduced_damage)

    def __repr__(self) -> str:
        return f"<Warrior name={self.name}, hp={self.hp}, armor={self.armor}, weapon={self.weapon}>"


class Mage(Character):
    """Represents a resource-based attacker Mage character[cite: 3]"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, weapon: Weapon = None, mana: int = 30, mana_max: int = 30) -> None:
        super().__init__(name, hp_max, damage, weapon)
        self.mana = mana         
        self.mana_max = mana_max 

    def attack(self, target) -> None:
        """Attacks target using magic if enough mana, otherwise falls back to base weapon attack and restores mana[cite: 3]"""
        if self.mana >= 10:
            self.mana -= 10  
            inflicted_damage = self.damage * 2
            target.take_damage(inflicted_damage)
        else:
            self.mana = min(self.mana + 5, self.mana_max)
            super().attack(target)

    def __repr__(self) -> str:
        return f"<Mage name={self.name}, hp={self.hp}, mana={self.mana}/{self.mana_max}, weapon={self.weapon}>"