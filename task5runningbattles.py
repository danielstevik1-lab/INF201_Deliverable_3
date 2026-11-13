""" ----- Task 5 ----- run battles ----- """

from character import Character, Warrior, Mage

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

    # --- KJØRING AV KAMP (TEST) ---
if __name__ == "__main__":
    from dice import Dice
    from items import Weapon

    # Lag en terning og et våpen
    sword_dice = Dice(6)
    sword = Weapon("Iron Sword", sword_dice)

    # Opprett en helt (Warrior) og en fiende (Mage)
    hero = Warrior(name="Aragorn", hp_max=100, damage=12, weapon=sword, armor=6)
    enemy = Mage(name="Saruman", hp_max=90, damage=15, mana=30)

    # Start kampen ved hjelp av Battle-klassen
    game_battle = Battle(hero, enemy)
    game_battle.simulate_battle()