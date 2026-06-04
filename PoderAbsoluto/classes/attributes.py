from PoderAbsoluto.classes import xp
import math
class Attributes(xp.Xp):
    def __init__(self, attribute, socialAttribute, aspects, level, xpNow, xpMax):
        super().__init__(xpNow, xpMax, level)
        self.attr = attribute
        self.sAttr = socialAttribute
        self.aspec = aspects
        self.level = level
        self.xp = xpNow
        self.xpMax = xpMax

        self.str = self.aspec['Força']
        self.agi = self.aspec['Agilidade']
        self.vit = self.aspec['Vitalidade']
        self.int = self.aspec['Inteligência']
        self.wil = self.aspec['Vontade']
        self.pre = self.aspec['Presença']

        self.strMod = math.ceil((self.aspec['Força'] - 10) / 2)
        self.agiMod = math.ceil((self.aspec['Agilidade'] - 10) / 2)
        self.vitMod = math.ceil((self.aspec['Vitalidade'] - 10) / 2)
        self.intMod = math.ceil((self.aspec['Inteligência'] - 10) / 2)
        self.wilMod = math.ceil((self.aspec['Vontade'] - 10) / 2)
        self.preMod = math.ceil((self.aspec['Presença'] - 10) / 2)

    def upgrade(self, attribute, quant=0):
        sAttr_list = ('Reputação', 'Infâmia', 'Notoriedade')
        aspec_list = ('Força', 'Agilidade', 'Vitalidade', 'Inteligência', 'Vontade', 'Presença')
        if attribute in sAttr_list:
            self.sAttr[attribute] += quant
        elif attribute in aspec_list:
            self.aspec[attribute] += quant
        else:
            self.attr[attribute] += quant

    def show_aspects(self):
        print('=======ASPECTOS=======')
        print(f'''[FOR]{self.str}(+{self.strMod})
[AGI]{self.agi}(+{self.agiMod})
[VIT]{self.vit}(+{self.vitMod})
[INT]{self.int}(+{self.intMod})
[VON]{self.int}(+{self.intMod})
[PRE]{self.pre}(+{self.preMod})''')

    def aspecMod(self, aspect):
        aspecMod = (self.aspec[aspect] - 10)/2
        return aspecMod

    def strMod(self):
        strMod = (self.aspec['Força'] - 10)/2
        self.attr['Physical Damage'] += strMod
