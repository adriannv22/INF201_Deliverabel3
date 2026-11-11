import random 

class Dice: 
    """"""
    def __init__(self, sides: int = 6): #Definere sider. int = 6 betyr default er lik 6. 
        """"""
        if sides >= 2:
            self.sides = sides

    def roll(self):
        """"""
        return random.randint(1, self.sides)

    def __repr__(self) -> str:
        """"""
        return f"Dice(sides = {self.sides})"
     
    def __call__(self):
        """"""
        return self.roll()

# Med å kalle på Dice classen kan vi selv bestemme hvor 
#mange sider terningen vi bruker i spillet har. 
#Oppgave 5 skrives i jupyter notebook. 

