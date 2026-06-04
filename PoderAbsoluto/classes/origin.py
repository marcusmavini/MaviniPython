from PoderAbsoluto.classes import player


class Origin(player.Attributes):
    def __init__(self, name, description, hp, nrg, dmg):
        super().__init__(hp, nrg, dmg)
        self.name = name
        self.desc = description

    def stats(self):
        print(f'''==={self.name}===
{self.desc}
HP      :+{self.hp}
DANO    :+{self.dmg}
ENERGIA :+{self.nrg}''')

    def gain_attr(self):


