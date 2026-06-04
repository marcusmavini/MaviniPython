from PoderAbsoluto.classes import attributes, xp

class Player(attributes.Attributes, xp.Xp):
    def __init__(self, name, origin, classe, level, xpNow, xpMax, aspects, attribute, socialAttribute, chip='Nenhum'):
        super().__init__(attribute, socialAttribute, aspects, level, xpNow, xpMax)
        self.name = name
        self.origin = origin
        self.classe = classe
        self.level = level
        self.xp = xpNow
        self.xpMax = xpMax
        self.attr = attribute
        self.sAttr = socialAttribute
        self.aspec = aspects
        self.chip = chip

    def stats(self):
        print(f'''======{self.name}======
ORIGEM: {self.origin}
CLASSE: {self.classe}
NÍVEL: {self.level}
XP {self.xp}/{self.xpMax}
{self.show_aspects()}
=====ATRIBUTOS SOCIAIS=====
{self.sAttr}
=====CHIP=====
>> {self.chip}
-------------------------------------------''')
