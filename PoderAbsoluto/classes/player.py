import math

class Player:
    def __init__(self, name, origin, classe,
                 level, xpNow, xpMax,
                 attribute, aspects, socialAttribute,
                 chip='Nenhum'):
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
# =========================================================
# ATRIBUTOS
# =========================================================
    def upgrade(self, attribute, quant=0): # Atualiza um atributo, atributo social ou aspecto
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
        print(f'''[FOR]{self.attr['Strenght']}(+{math.ceil((self.attr['Strenght'] - 10) / 2)})
[AGI]{self.attr['Agility']}(+{math.ceil((self.attr['Agility'] - 10) / 2)})
[VIT]{self.attr['Vitality']}(+{math.ceil((self.attr['Vitality'] - 10) / 2)})
[INT]{self.attr['Inteligence']}(+{math.ceil((self.attr['Inteligence'] - 10) / 2)})
[VON]{self.attr['Will']}(+{math.ceil((self.attr['Will'] - 10) / 2)})
[PRE]{self.attr['Presence']}(+{math.ceil((self.attr['Presence'] - 10) / 2)})''')
    
    def attr_mod(self, aspect, attribute):
        return self.aspec[aspect] + (self.attr[attribute]-10)/2
    
# =========================================================
# EXPERIÊNCIA
# =========================================================
    def show_level(self):
        print(f'--------------\nNÍVEL: {self.level}\n[XP]{self.xp}/{self.xpMax}')
        
        xp_percent = math.ceil((self.xp/self.xpMax)*100) # Calcula a parcetagem para atingir o próximo nível
        
        print(f'[===={xp_percent}%====]\n--------------')

    def gainXP(self, quant): # Ganha XP
        if self.xp < self.xpMax:
            self.xp += quant # Ganha somente se o XP atual for menor que o XP máximo
            print(f'Você ganhou {quant} de Pontos de Experiência')
            if self.xp >= self.xpMax: # Se, ao ganhar a quantidade de xp, o xp atual for maior ou igual ao xp máximo, evolui
                self.level += 1
                print(f'>> Passou de Nível! <<\n----Seu nível atual é {self.level}----')
                self.xpMax += int(self.xpMax * 0.55)
        else:
            self.level += 1 # Aqui faz o mesmo que no if anterior
            print(f'>> Passou de Nível! <<\n----Seu nível atual é {self.level}----')
            self.xpMax += int(self.xpMax * 0.55)
