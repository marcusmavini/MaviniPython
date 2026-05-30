class Origin:
    def __init__(self, name, description, hp, dmg, energy):
        self.name = name
        self.desc = description
        self.hp = hp
        self.dmg = dmg
        self.nrg = energy

    def stats(self):
        print(f'''==={self.name}===
{self.desc}
HP      :+{self.hp}
DANO    :+{self.dmg}
ENERGIA :+{self.nrg}''')


