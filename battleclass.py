""" ----- Task 5 ----- run battles ----- """

from character import Character, Warrior, Mage
from items import Weapon
from dice import Dice

class Battle:
    """Manages turn-based combat between two Character objects"""

    def __init__(self, hero: Character, enemy: Character) -> None:
        self.hero = hero
        self.enemy = enemy

    def play_round(self) -> None:
        """Executes a single combat round where hero attacks first, then enemy if still alive"""
        if self.hero.is_alive:
            self.hero.attack(self.enemy)
            print(f"{self.hero.name} angriper {self.enemy.name}! {self.enemy.name} har nå {self.enemy.hp} HP igjen.")

        if self.enemy.is_alive:
            self.enemy.attack(self.hero)
            print(f"{self.enemy.name} angriper {self.hero.name}! {self.hero.name} har nå {self.hero.hp} HP igjen.")

    def simulate_battle(self) -> Character:
        """Simulates turns in a while loop until one character is defeated, returns the winner"""
        print(f"--- Kampen starter mellom {self.hero.name} og {self.enemy.name}! ---")
        
        while self.hero.is_alive and self.enemy.is_alive:
            self.play_round()
            print("-" * 30)

        winner = self.hero if self.hero.is_alive else self.enemy
        print(f"🏆 {winner.name} har vunnet kampen!")
        return winner


