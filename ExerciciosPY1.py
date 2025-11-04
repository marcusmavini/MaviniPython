'''
Exercício 1: Olá, Mundo Personalizado
Problema: Crie um programa que pergunta o nome do usuário e exibe uma
mensagem de boas-vindas personalizada.
'''
name = input("Olá! Qual seu nome? ")
print(f"Seja bem vindo, {name}! Aqui você verá tudo sobre tecnologia")

'''
Exercício 2: Calculadora de Idade
Problema: Escreva um programa que calcula a idade de uma pessoa baseado
no ano de nascimento.
'''
ano_input = int(input("Em que ano você nasceu? "))
idade = 2025 - ano_input
print("Com base no ano que você nasceu...")
print(f"Você tem {idade} anos!")

'''
Exercício 3: Par ou Ímpar
Problema: Crie um programa que verifica se um número é par ou ímpar.
'''
numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print("Este número é PAR!")
else:
    print("Este número é IMPAR!")

'''
Exercício 4: Média de Três Notas
Problema: Calcule a média de três notas e determine se o aluno foi aprovado (média >= 7).
'''
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
print(f"A média do aluno foi {media:.2f}") ## :.2f indica somente duas casas decimais depois da vírgula, evitando uma sequencia de números iguais
if media >= 7:
    print("Aprovado!!")
else:
    print("Reprovado!")

'''
Exercício 5: Tabuada
Problema: Gere a tabuada de um número escolhido pelo usuário.
'''

numero = int(input("Digite um número para ver sua tabuada: "))
print(f"\nTabuada do {numero}:")
print("-" * 20)

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i:2} = {resultado}") ## O formato {i:2} alinha os números em duas posições, deixando a tabuada mais organizada.