# Salário de Funcionario e com 15% de aumento
"""
Entrada: Salário
Saída: Salário + 15%
"""
print('===DESAFIO 013===')

nome = input('Funcionário: ')
salario = float(input('Salário: R$'))

aumento = salario + (salario * 0.15)

print(f'Aumento: R${aumento:.2f}')