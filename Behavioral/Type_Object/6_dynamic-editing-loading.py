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
    def __init__(self, name, health, attack, parent=None):
        self._name = name
        self._parent = parent
        self._health = health
        self._attack = attack

    @property
    def name(self):
        return self._name

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
        if self.attack or self.parent == None:
            attack = self.attack
        else:
            attack = self.parent.getAttack()

        return attack

    def setParent(self, breed):
        self._parent = breed

    def __repr__(self):
        return "<{0} object with parent {1} - Health {2} - Attack {3}>".format(
            self.name,
            self.parent.name if self.parent else None,
            self.getHealth(),
            self.getAttack()
        )

    @classmethod
    def newMonster(cls, breed):
        monster = Monster(breed)
        return monster


if __name__ == '__main__':
    breeds_data = {
        "Troll": {
            "health": 25,
            "attack": "The troll hits you!"
        },
        "Troll Archer": {
            "parent": "Troll",
            "health": 0,
            "attack": "The troll archer fires an arrow!"
        },
        "Troll Wizard": {
            "parent": "Troll",
            "health": 0,
            "attack": "The troll wizard casts a spell on you!"
        }
    }

    # Breeds{} -> name: Breed(name, health, attack)
    breeds = {}

    # Pass 1: Build the Breed instances using the name, health and attack properties
    # Parenting relationships will be setup in the second pass
    for name, data in breeds_data.iteritems():
        health = data.get('health')
        attack = data.get('attack')
        breed = Breed(name, health, attack)
        breeds[name] = breed


    # Pass 2: Set up the parenting relationships
    for name, data in breeds_data.iteritems():
        parent_name = data.get('parent')
        if not parent_name:
            continue

        parent = breeds.get(parent_name)
        child = breeds.get(name)

        child.setParent(parent)

    # Breed instances are now ready to be used.

    print breeds
    breeds.get('Troll Archer')
    print breeds.get('Troll Archer').health
    breeds.get('Troll Archer')._health = 10
    print breeds
    breeds.get('Troll')._health = 100
    print breeds
