# Object-oriented game simulator
# Turid Torheim, NMBU, 2026

class Character:
    """Represents a character in the RPG"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10) -> None:
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

    def attack(self, target) -> None:
        """Attack and deal damage to target character"""
        target.take_damage(self.damage)

    def introduce(self) -> None:
        """Creates string that introduces character"""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of character object"""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>)"

    def __str__(self) -> str:
        """String representation of character object"""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"

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


class Worrior(Character):
    """"""
    def __init__(self, name, hp_max = 100, damage = 10, armor: int = 5) -> None:
        """"""
        super().__init__(name, hp_max, damage)
        self.armor=armor

    @property
    def take_damage(self, amount: int) -> None:
            """Reduce character's HP by a specified amount"""
            self._hp -= amount
            self._hp = max(self._hp, 0)  # Ensure HP does not go below 0

class Mage(Character):
    """"""
    def __init__(self, name, hp_max = 100, damage = 10, mana: int = 30, mana_max: int = 30) -> None:
        """"""
        super().__init__(name, hp_max, damage)
        self.mana = mana
        self.mana_max = mana_max

    def attack(self, target) -> None:
            """Attack and deal damage to target character"""
            if self.mana >= 10:
                target.take_damage(self.damage)
            else:
                target.take_damage(self.damage)

wn = Worrior("kn")
mn = Mage("mn")

print(mn._hp)

wn.attack(mn)

print(mn._hp)

mn.attack(wn)

print(wn._hp)