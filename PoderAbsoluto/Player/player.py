import inspect

class Player:
    def __init__(self, name, origin, classe,
                 health, energy, damage, defense, power,
                 chip='Nenhum'):
        self.name = name
        self.origin = origin
        self.classe = classe
        self.hp = health
        self.nrg = energy
        self.dmg = damage
        self.df = defense
        self.pw = power
        self.chip = chip
        self.attr = [self.hp, self.nrg, self.dmg, self.df, self.pw]

    def stats(self):
        print(f'''======{self.name}======
ORIGEM: {self.origin}
CLASSE: {self.classe}
=====ATRIBUTOS=====
VIDA: {self.hp}
ENERGIA: {self.nrg} 
DANO: {self.dmg}
DEFESA: {self.df}
PODER: {self.pw}
=====CHIP=====
>> {self.chip}
-------------------------------------------''')

    def hp_mod(self, modifier, amount):
        if modifier == 'up':
           self.hp += amount
        elif modifier == 'down':
           self.hp -= amount
        elif modifier == 'define':
            attr_hist = self.hp
            self.hp = amount
            print(f'O HP foi alterado de {attr_hist} para {self.hp}')

    def nrg_mod(self, modifier, amount):
        if modifier == 'up':
           self.nrg += amount
        elif modifier == 'down':
           self.nrg -= amount
        elif modifier == 'define':
            self.nrg = amount

    def attr_up(self, attribute, quant=0):
        #attr_list_str = ['hp', 'nrg', 'dmg', 'df', 'pw']
        assinatura = inspect.signature(Player.__init__)
        attr_list = list(assinatura.parameters.keys())

        if attribute in attr_list:
            print('Achei')
        else:
            print('Ainda não xxxxxx')
            print(attr_list)