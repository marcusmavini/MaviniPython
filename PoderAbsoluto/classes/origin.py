class Origin:
    def __init__(self, code, name, description, requirements,
                 attribute, aspects, socialAttribute,
                 passives, improvements):
        self.code = code
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
                

class OriginPassives:
    def __init__(self, name, description, action, attribute, aspects, socialAttribute):
        self.name = name
        self.desc = description
        self.action = action
        self.attr = attribute
        self.aspects = aspects
        self.sAttr = socialAttribute