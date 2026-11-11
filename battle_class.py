from game_simulator_v1_1 import Character, Warrior, Mage

class Battle:
    """"""

    def __init__(self, hero: Character, enemy: Character) -> None:
        """"""
        self.hero = hero
        self.enemy = enemy

    def play_around(self) -> None:
        """"""
        #Hero attacks enemy
        self.hero.attack(self.enemy)
        #If enemy is still alive, enemy attacks hero 
        if self.enemy.is_alive():
            self.enemy.attack(self.hero)

    def simulate_battle(self) -> None:
        """"""
        round_number: int = 1

        while self.hero.is_alive() and self.enemy.is_alive():
            print()
            self.play_round()
            round_number += 1

        print()
        if self.hero.is_alive():
            print()
        else:
            print()
