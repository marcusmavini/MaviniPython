
class Attributes:
    def __init__(self, hp, energy, dmg):
        self.hp = hp
        self.nrg = energy
        self.dmg = dmg

    def show_all(self):
        print(f'''======Todos os Atributos======
HP      :{self.hp}
DANO    :{self.dmg}
ENERGIA :{self.nrg}''')


class Player(Attributes):
    def __init__(self, name, xp, attributes, inventory):
        super().__init__(hp, nrg, dmg)
        self.name = name
        self.xp = xp
        self.hp = super().hp
        self.attr =
        self.inv = inventory

    def stats(self):
        print(f'====Jogador: {self.name}')
        self.show_all()