from game_simulator_v1_1 import Character, Warrior, Mage

class Battle:
    """Create the turnbased battle between two characters in the RPG."""

    def __init__(self, hero: Character, enemy: Character) -> None:
        """
        Initialise the Battle
        
        Args:
            hero (Character): The character who is the hero in the battle.
            enemy (Character): The character who is the enemy in the battle. 
        """
        self.hero = hero
        self.enemy = enemy

    def play_round(self) -> None:
        """
        For each round the hero first attacks the enemy, and if enemy is alive, 
        the enemy attacks the hero
        """
        #Hero attacks enemy
        self.hero.attack(self.enemy)

        #If enemy is still alive, enemy attacks hero 
        if self.enemy.is_alive():
            self.enemy.attack(self.hero)

    def simulate_battle(self) -> None:
        """Simulate the battle with one or more rounds until one character dies."""
        round_number: int = 1 #The battle starts with round number 1

        # A while loop that runs rounds until one character is defeated
        while self.hero.is_alive() and self.enemy.is_alive():
            print(f"Round {round_number}")
            self.play_round()
            round_number += 1 

        # When the loop breaks we announce the winner
        print("Battle is finished")
        if self.hero.is_alive():
            print(f"{self.hero.name} wins the battle!")
        else:
            print(f"{self.enemy.name} wins the battle!")
