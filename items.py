from dice_class import Dice

class Weapon:
    """This class uses the Dice class to calculate damage."""

    def __init__(self, name: str, damage_dice: Dice) -> None: #damage_dice er et objekt som f.eks d20 som du lager
        """
        Initialise a weapon
        
        Args:
            name (str): The name of the character.
            damage_dice (Dice): Damage delt when character attacks (default = 10)
        """
        self.name: str = name
        self.damage_dice = damage_dice

    def roll_damage(self) -> int:
        """"""
        return self.damage_dice.roll()

    #Hvis f.eks. en 10 sidet terning ruller og gir 10, vil karakteren miste 10 hp. 

        
