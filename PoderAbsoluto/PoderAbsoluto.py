import passiveSkills
raridades = ('Comum', 'Incomum', 'Raro', 'Épico', 'Ledário', 'Super')

perfilHeroi = {'nome': input("Nome: "),
               'origem': input("Origem: "),
               'localidade': input("localidade: "),

               'hp':500,
               'mana':50,
               'dmg':30,
               'def':10
}

def resultvictorybattle(nameheroi, nameinimigo,dmg):
    print(f'{nameheroi} derrotou {nameinimigo}!')
    escolhainfobatt = input('Mostrar informações da batalha?')
    if escolhainfobatt == 'sim':
        print(f'Foi causado {dmg} de dano!')

inimigo1 = {
    'nome': 'Ladrão',
    'hp':230,
    'mana':40,
    'dmg':10,
}

passiveSkills.pssv_queimadura_pirocinese(perfilHeroi['dmg'],inimigo1['hp'])

chipPirocinese = {
    'nome': 'Pirocinese',
    'raridade': 'Comum',
    'resonancia': 'Otimizado',

    'dmg':20,
    'dmgFogo': 5
}

print(perfilHeroi)

print("===ESCOLHA SEU PODER===")
escolhaPoder = input("(1) Fogo\n(2) Gelo\n(3) Eletricidade\n")

while escolhaPoder == "1" or escolhaPoder == "2" or escolhaPoder == "3":
    if escolhaPoder == "1":
        print("Você escolheu o poder do Fogo!")
        perfilHeroi['poder'] = 'fogo'
    elif escolhaPoder == "2":
        print("Você escolheu o poder do Gelo!")
        perfilHeroi['poder'] = 'gelo'
    elif escolhaPoder == "3":
        print("Você escolheu o poder da Eletricidade!")
        perfilHeroi['poder'] = 'eletricidade'
    break
else:
    print("Número incorreto")

print(perfilHeroi)







'''

print(raridades)
print(raridades[1])

fogoComum = {'dano':30, 'raridade':raridades[0]}
inimigo1 = {'vida':100, 'dano':22}

luta = int(inimigo1['vida'] - fogoComum['dano'])

print(luta)

print(f"A raridade do fogo é {fogoComum['raridade']}")
'''
