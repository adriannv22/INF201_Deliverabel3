# Object-oriented game simulator
# Turid Torheim, NMBU, 2026

from items import Weapon 
from dice_class import Dice

class Character:
    """Represents a character in the RPG"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, weapon: Weapon = None) -> None:
        """
        Initialise the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage delt when character attacks (default = 10)

        """
        self.name = name
        self._hp = hp_max  # Note: _hp indicated private attribute
        self.hp_max = hp_max
        self.damage = damage
        self.weapon = weapon

    def attack(self, target) -> None:
        """Attack and deal damage to target character"""
        if self.weapon != None:
            target.take_damage(self.weapon.roll_damage())
        else:   
            target.take_damage(self.damage)

    def introduce(self) -> None:
        """Creates string that introduces character"""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of character object"""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>)"

    def __str__(self) -> str:
        """String representation of character object"""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage and weapon {self.weapon}"

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits."""
        return self._hp

    def is_alive(self) -> bool:
        """Check if character is alive (hp > 0)"""
        return self._hp > 0

    def take_damage(self, amount: int) -> None:
                """Reduce character's HP by a specified amount"""
                self._hp -= amount
                self._hp = max(self._hp, 0)  # Ensure HP does not go below 0
    

class Warrior(Character):
    """"""
    def __init__(self, name, hp_max = 100, damage = 10, armor: int = 5, weapon: Weapon = None) -> None:
        """"""
        super().__init__(name, hp_max, damage, weapon)
        self.armor=armor

    def take_damage(self, amount: int) -> None:
            """Reduce character's HP by a specified amount"""
            #The if statment makes sore the the damaging atack don't add hp
            if amount > self.armor:
                self._hp -= amount - self.armor
                self._hp = max(self._hp, 0)  # Ensure HP does not go below 0

class Mage(Character):
    """"""
    def __init__(self, name, hp_max = 100, damage = 10, mana: int = 30, mana_max: int = 30, weapon: Weapon = None) -> None:
        """"""
        super().__init__(name, hp_max, damage, weapon)
        self.mana = mana
        self.mana_max = mana_max

    def attack(self, target) -> None:
        """Mage bruker mana for å gjøre ekstra skade, eller svakere angrep hvis tom for mana"""
        if self.weapon != None:
             damage = self.weapon.roll_damage()
        else:
             damage=self.damage
        
        if self.mana >= 10:
            self.mana -= 10
            target.take_damage(damage*2)
        else:
            self.mana += 5
            target.take_damage(damage)
