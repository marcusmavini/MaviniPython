"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = eval(input('Que horas são?\n'))

if hora >= 0 and hora <= 11:
    print(f'[{hora}:00] Bom dia!')
elif hora > 11 and hora <= 17:
    print(f'[{hora}:00] Boa Tarde!')
else:
    print(f'[{hora}:00] Boa Noite!')