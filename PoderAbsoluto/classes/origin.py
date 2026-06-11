import attributes

class Origin(attributes.Attributes):
    def __init__(self, name, description, requirements, attribute, aspects, socialAttribute, passives, improvements):
        super().__init__(attribute, socialAttribute, aspects)
        self.name = name
        self.desc = description
        self.require = requirements
        self.attr = attribute
        self.aspects = aspects
        self.sAttr = socialAttribute
        self.pssv = passives
        self.improv = improvements
        
    
    def statsO(self):
        print(f'''Origem: {self.name}
Descrição: {self.desc}
== Passiva: {self.pssv.name} ==
Descrição: {self.pssv.desc}
{self.attr}
{self.sAttr}
{self.aspects}
------''')
        
    def getPssv(self, passive):
        for attribute in passive.attr:
            if attribute in self.attr:
                self.attr[attribute] += passive.attr[attribute]
            else:
                self.attr[attribute] = passive.attr[attribute]
                

class Passives:
    def __init__(self, name, description, action, attribute, aspects, socialAttribute):
        self.name = name
        self.desc = description
        self.action = action
        self.attr = attribute
        self.aspects = aspects
        self.sAttr = socialAttribute


pssvHumano = Passives(
    'Misturado',
    'Consegue se encaixar em qualquer lugar.',
    '',
    {
        'Presence':2,
        'Strenght':8
    },
    {
        'Health':24,
        'Energy':380
    },
    {
        'Reputation':2
    }
)

humano = Origin(
    'Humano',
    'Um ser humano normal',
    '',
    {
        'Presence':1,
        'Inteligence':1,
    },
    {
        'Health':57,
        'Physical Damage':27,
    },
    {
        'Notoriety':1,
    },
    pssvHumano,
    '',
)
humano.statsO()
humano.getPssv(pssvHumano)
humano.statsO()