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


class Breed(object):
    def __init__(self, health, attack, parent=None):
        self._parent = parent
        self._health = health
        self._attack = attack

    @property
    def parent(self):
        return self._parent

    @property
    def health(self):
        return self._health

    @property
    def attack(self):
        return self._attack

    def getHealth(self):
        if not self.health == 0 or self.parent == None:
            health = self.health
        else:
            health = self.parent.getHealth()

        return health

    def getAttack(self):
        if not self.attack or self.parent == None:
            attack = self.attack
        else:
            attack = self.parent.getAttack()

        return attack

    @classmethod
    def newMonster(cls):
        breed = cls(100, "Yayayayayaya")
        monster = Monster(breed)
        return monster

