from game_simulator_v1_1 import Character, Warrior, Mage

class Battle:
    """"""

    def __init__(self, hero: Character, enemy: Character):
        """"""
        self.hero = hero
        self.enemy = enemy

    def play_around(self):
        """"""
        #Hero attacks enemy
        self.hero.attack(self.enemy)
        #If enemy is still alive, enemy attacks hero 
        if self.enemy.is_alive():
            self.enemy.attack(self.hero)
            hero.take_damage(self.damage)


    def simulate_battle(self):
        """"""
        while self.hero.is_alive() and self.enemy.is_alive():
            self.play_round()
            round_num += 1

        print()
        if self.hero.is_alive():
            print()
        else:
            print()
