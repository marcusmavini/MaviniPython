# Quantidade de metros convertido em centimetros e milimetros
"""
Entrada: Número em metros
Saída: Conversão em centimetros e milimetros
"""
print('===DESAFIO 008===')

metros = float(input('Digite um número: '))
convCentimetros = metros * 100
convMilimetros = metros * 1000

print(f'Conversão de {metros}m:\nCentímetros >> {convCentimetros:.1f}\nMilimetros >> {convMilimetros}')