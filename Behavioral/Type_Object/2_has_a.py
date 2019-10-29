"""

Each monster in the game is simply an instance of class Monster

The Breed class contains the information that's shared between all the monsters of the same breed
    - Starting Health
    - Attack String

Each Monster instance is given a reference to a Breed object containing the information for that breed.

Define a TYPE OBJECT class and a TYPED OBJECT class.

Each TYPE OBJECT instance represents a different logical type.
    Data or behavior that should be shared across all instances of the same conceptual type is stored in
    the TYPE OBJECT

Each TYPED OBJECT stores a reference to the type object that describes its type.
    Instance specific data is stored in the typed object instance
"""


class Breed(object):
    def __init__(self, health, attack):
        self._health = health
        self._attack = attack

    @property
    def health(self):
        return self._health

    @property
    def attack(self):
        return self._attack

    def getHealth(self):
        return self.health

    def getAttack(self):
        return self.attack


class Monster(object):
    def __init__(self, breed):
        self._health = breed.getHealth()
        self._breed = breed

    @property
    def health(self):
        return self._health

    @property
    def breed(self):
        return self._breed

    def getAttack(self):
        return self.breed.getAttack()
