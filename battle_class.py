from game_simulator_v1_1 import Character, Warrior, Mage

class Battle:
    """"""

    def __init__(self, hero: Character, enemy: Character):
        """"""
        self.hero = hero
        self.enemy = enemy

    def play_around(self, hero, enemy):
        """"""
        enemy.take_damage(self.damage)
        if self._hp > 0:
            hero.take_damage(self.damage)


    def simulate_battle(self):
        """"""
        while :