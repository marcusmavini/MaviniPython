from PoderAbsoluto.Origins.origin import Origin

class Human(Origin):
    def __init__(self, name, description, hp, dmg, energy):
        super().__init__(name, description, hp, dmg, energy)
        self.name = 'Humano'
        self.description = 'Um humano simples'
        self.hp = 1000
        self.dmg = 50
        self.nrg = 100