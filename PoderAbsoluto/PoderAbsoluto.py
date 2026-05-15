import tkinter as tk
from tkinter import messagebox
root = tk.Tk()


messagebox.showinfo('Poder Absoluto', 'Bem vindo ao jogo!')

rarity = ['Comum', 'Incomum', 'Raro', 'Épico', 'Lendário', 'Super']
resonance = ['Instável', 'Bruto', 'Ajustado', 'Refinado', 'Otimizado', 'Avançado', 'Perfeito', 'Super']
origin = ['Padrão', 'Titânico', 'Condutor']

print("==== PODER ABOSOLUTO ===")
print("Você é o Herói!")
print("-"*20)
print("Vamos criar o perfil do seu herói.")

heroProfile = {'nome': '',
               'origem': '',
               'localidade': '',

               'hp':'',
               'mana':'',
               'dmg':'',
               'def':'',
               'agi':'',

               'chip':'',
}

# Escolher Origem
print("Selecione a Origem:")
print("===HUMANO===>"
      "Humanos comuns que despertaram potencial através de treinamento,\nexperiência ou adaptação extrema.\n"
      "Vantagens:\n- Evolução versátil\n- Facilidade em aprender perícias\n- Boa adaptação a qualquer classe\n- Progressão equilibrada\n")
print("===TITÂNICO===>"
      "Titânicos costumam possuir estrutura óssea extremamente densa, musculatura anormal e\ncapacidade absurda de suportar dor e continuar lutando mesmo após danos severos.\n"
      "Vantagens:\n- Altíssima resistência física\n- Grande quantidade de vida\n- Força brutal em combate corpo a corpo\n- Resistência elevada a atordoamento e impacto\n")
print("===CONDUTOR===>"
      "Condutores tem uma capacidade anormal de canalizar, armazenar e transferir energia.\nEles não necessariamente criam energia — eles captam, amplificam e redirecionam.\n"
      "Vantagens:\n- Melhor controle e eficiência energética\n- Resistência parcial a dano energético\n- Alto potencial ofensivo e de sustentação\n- Maior estabilidade ao usar chips poderosos")
print("Leia atentamente cada uma e escolha sua origem.")

originChoice = input("(1) Humano\n(2) Titânico\n(3) Condutor\n")
if originChoice == "1":
    yon = input("(1) Confirma\n(9) Voltar\n")
    if yon == "1":
        heroProfile['origem'] = 'Humano'
        print("Parabéns. Você escolheu a origem mais imprevisível de todas.\nHumanos não possuem corpos perfeitos, poderes naturais absurdos ou vantagens genéticas garantidas.\nAinda assim, foram eles que construíram tecnologias, enfrentaram monstros, desafiaram entidades cósmicas e\nsobreviveram a mundos em colapso.\n")
elif originChoice == "2":
    yon = input("(1) Confirma\n(9) Voltar")
    if yon == "1":
        heroProfile['origem'] = 'Titânico'
        print("Parabéns. Você escolheu carregar o peso da destruição.\nTitânicos não foram feitos para recuar.\nSeus corpos suportam impactos que destruiriam veículos, atravessam combate direto sem hesitar e\ntransformam força bruta em domínio absoluto do campo de batalha.")


chipPirocinese = {
    'nome': 'Pirocinese',
    'raridade': rarity[0],
    'resonancia': resonance[5],

    'dmg':20,
    'dmgFogo': 5,
    'psv': '',
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

print(heroProfile)

print("===ESCOLHA SEU PODER===")
escolhaPoder = input("(1) Fogo\n(2) Gelo\n(3) Eletricidade\n")

while escolhaPoder == "1" or escolhaPoder == "2" or escolhaPoder == "3":
    if escolhaPoder == "1":
        print("Você escolheu o poder do Fogo!")
        heroProfile['poder'] = 'fogo'
    elif escolhaPoder == "2":
        print("Você escolheu o poder do Gelo!")
        heroProfile['poder'] = 'gelo'
    elif escolhaPoder == "3":
        print("Você escolheu o poder da Eletricidade!")
        heroProfile['poder'] = 'eletricidade'
    break
else:
    print("Número incorreto")

print(heroProfile)







'''

print(raridades)
print(raridades[1])

fogoComum = {'dano':30, 'raridade':raridades[0]}
inimigo1 = {'vida':100, 'dano':22}

luta = int(inimigo1['vida'] - fogoComum['dano'])

print(luta)

print(f"A raridade do fogo é {fogoComum['raridade']}")
'''
root.mainloop()