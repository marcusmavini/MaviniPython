# Quanto dinheiro tem e quantos dolares pode comprar (1 dolar = 4,96)
"""
Entrada: Quantide de dinheiro
Saída: Quantos dolares pode comprar
"""
print('===DESAFIO 010===')

dinheiro = float(input('Quanto de dinheiro você tem? R$ '))
dolar = dinheiro / 4.96

print(f'Com este valor, você consegue comprar US${dolar:.2f}')