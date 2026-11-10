
class Weapon:
    """"""
    
    def __init__(self, name, damage_dice: Dice):
        """"""
        self.name = name
        self.damage_dice = damage_dice

    def roll_damage(self):
        """"""
        self.damage_dice.roll()

        
