import abc


class Monster(object):
    def __init__(self, startingHealth):
        self._health = startingHealth

    @property
    def health(self):
        return self._health

    @abc.abstractmethod
    def getAttack(self):
        pass


class Dragon(Monster):
    def __init__(self):
        super(Dragon, self).__init__(230)

    def getAttack(self):
        return "The dragon breathes fire!"


class Troll(Monster):
    def __init__(self):
        super(Troll, self).__init__(48)

    def getAttack(self):
        return "The troll clubs you!"

