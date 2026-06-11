import math
class Attributes:
    def __init__(self, attribute, socialAttribute, aspects):
        self.attr = attribute
        self.sAttr = socialAttribute
        self.aspec = aspects
        
        #self.str = self.attr['Strenght']
       # self.agi = self.attr['Agility']
        #self.vit = self.attr['Vitality']
        #self.int = self.attr['Inteligence']
        #self.wil = self.attr['Will']
        #self.pre = self.attr['Presence']
    '''
        self.strMod = math.ceil((self.attr['Strenght'] - 10) / 2)
        self.agiMod = math.ceil((self.attr['Agility'] - 10) / 2)
        self.vitMod = math.ceil((self.attr['Vitality'] - 10) / 2)
        self.intMod = math.ceil((self.attr['Inteligence'] - 10) / 2)
        self.wilMod = math.ceil((self.attr['Will'] - 10) / 2)
        self.preMod = math.ceil((self.attr['Presence'] - 10) / 2)'''

    def upgrade(self, attribute, quant=0):
        sAttr_list = ('Reputation', 'Infamy', 'Notoriety')
        attr_list = ('Strenght', 'Agility', 'Vitality', 'Inteligence', 'Will', 'Presence')
        if attribute in sAttr_list:
            self.sAttr[attribute] += quant
        elif attribute in attr_list:
            self.attr[attribute] += quant
        else:
            self.aspec[attribute] += quant

    def show_attr(self):
        print('=======ATRIBUTOS=======')
        print(f'''[FOR]{self.str}(+{self.strMod})
[AGI]{self.agi}(+{self.agiMod})
[VIT]{self.vit}(+{self.vitMod})
[INT]{self.int}(+{self.intMod})
[VON]{self.int}(+{self.intMod})
[PRE]{self.pre}(+{self.preMod})''')
    
    def attr_mod(self, aspect, attribute):
        return self.aspec[aspect] + (self.attr[attribute]-10)/2