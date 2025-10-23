# Input de dois números
numero1 = input('Escreva um número: ')
numero2 = input('Escreva outro número: ')

num1 = int(numero1)
num2 = int(numero2)

# Matemática simples
soma = num1 + num2
subt = num2 - num1
multi = num1 * num2
divi = num2 / num1

print(f'Soma: {soma} | Subtração: {subt} | Multiplicação: {multi} |  Divisão: {divi}')

# Qual número é maior?
if(num1 == num2):
    print('Os números são iguais')
if(num1 > num2):
    print(f'O número {num1} é o maior número!')
else:
    print(f'O número {num2} é o maior número!')