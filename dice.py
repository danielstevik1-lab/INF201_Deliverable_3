import random as rd

class Dice:
    """Represents the dice that will be used in the game"""


    def __init__(self, sides: int = 6):
        """Initialize dice
        Args:
            sides(int):        Amount of sides on dice, default value = 6 (standard dice)"""
        if sides < 2:
            raise ValueError("Minimum amount of sides on dice = 2")
        
        self.sides = sides
        


    def roll(self) -> int:
        """Roll the dice! Returns a random number between 1 and the total amount of sides on the dice"""
        return rd.randint(1, self.sides)


    def __repr__(self)->str:
        """Representation of dice object"""
        return f"Dice(sides = {self.sides})"


    def __call__(self) -> int:
        """Allows the object to be called as function"""
        return self.roll()

d20 = Dice(20)
d6 = Dice()
print(d6, ',', d20)
print(d6(),',',d20())

