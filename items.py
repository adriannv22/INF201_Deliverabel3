from dice_class import Dice


class Weapon:
    """This class uses the Dice class to calculate damage."""

    def __init__(self, name: str, damage_dice: Dice) -> None:
        """
        Initialise a weapon
        
        Args:
            name (str): The name of the weapon
            damage_dice (Dice): damage_dice is an object for example d20 with 20 sides
        """
        self.name: str = name
        self.damage_dice = damage_dice

    def roll_damage(self) -> int:
        """Roll the weapon's damage_dice and return the damage value"""
        return self.damage_dice.roll() #The returned damage value is an integer.

        