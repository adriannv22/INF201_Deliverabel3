import random 

class Dice: 
    """"""
    def __init__(self, sides: int = 6) -> None: #Definere sider. int = 6 betyr default er lik 6. 
        """"""
        if sides >= 2:
            self.sides: int = sides

    def roll(self) -> int:
        """"""
        return random.randint(1, self.sides)

    def __repr__(self) -> str:
        """"""
        return f"Dice(sides = {self.sides})"
     
    def __call__(self) -> int:
        """"""
        return self.roll()

# Med å kalle på Dice classen kan vi selv bestemme hvor 
#mange sider terningen vi bruker i spillet har. 
#Oppgave 5 skrives i jupyter notebook. 

d20 = Dice(sides = 20)
print(d20.roll())