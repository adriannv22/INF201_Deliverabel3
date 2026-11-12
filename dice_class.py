import random 


class Dice: 
    """A dice which makes the damage dealt by the characters variable"""

    def __init__(self, sides: int = 6) -> None: 
        """
        Initialise the Dice
                
        Args:
            sides (int): n-sided Dice (default = 6)
        """
        if sides >= 2: #The dice must have at least 2 sides
            self.sides: int = sides

    def roll(self) -> int:
        """Roll the dice and get a random integer"""
        return random.randint(1, self.sides)

    def __repr__(self) -> str:
        """Representation of dice object"""
        return f"Dice(sides = {self.sides})"
     
    def __call__(self) -> int:
        """This method allows the dice object to be called like a function"""
        return self.roll()

# When we call the Dice class, we can decide how 
# many sides the dice in the RPG has.  
