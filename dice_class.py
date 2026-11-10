import random 

class Dice: 
    """"""
    def __init__(self, sides: int): #Definere sider 
        """"""
        if sides >= 2:
            self.sides = sides

    def roll(self):
        """"""
        random.randint(1, self.sides)

    def __repr__(self) -> str:
        """"""
        return Dice(sides)
     
    def __call__(self):
        """"""
        return 