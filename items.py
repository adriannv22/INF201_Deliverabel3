from dice_class import Dice

class Weapon:
    """"""

    def __init__(self, name: str, damage_dice: Dice): #damage_dice er et objekt som f.eks d20 som du lager
        """"""
        self.name = name
        self.damage_dice = damage_dice

    def roll_damage(self):
        """"""
        return self.damage_dice.roll()

    #Hvis f.eks. en 10 sidet terning ruller og gir 10, vil karakteren miste 10 hp. 

        
