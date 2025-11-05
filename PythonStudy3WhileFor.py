## While

i = 0
while True:
    print(i)
    i += 1
    if i >= 5:
        break
print("Olá! Tudo bem? Meu nome é MavBot")

## For
counter = 0
for counter in range(5):
    print(counter)
    counter += 1 
print("Olá! Tudo bem? Meu nome é MavBot")

## For com lista
lista = ["Mavini", "Python", "Estudo", "Enquanto", "Para"]
for item in lista:
    print(item) 
    if item == "Enquanto":
        print("Achei o item 'Enquanto' na lista!") 
    continue
print("Fim da lista!")

## Contar de 1 até 10 (acertei)
counter = 0
print("Vamos contar até 10!")
while counter < 10:
    counter += 1
    print(counter)

## Contar de 10 até 1 (acertei)
counter = 10
print("Agora vamos contar de 10 até 1!")
while counter > 0:
    print(counter)
    counter -= 1

## o programa deve somar vários números digitados até que o usuário digite 0 (esse eu copiei, não consegui fazer)
soma = 0
numero = int(input("Digite um número (0 para parar): "))

while numero != 0:
    soma += numero
    numero = int(input("Digite outro número (0 para parar): "))

print("A soma total é:", soma)

## o programa escolhe um número e o usuário tenta adivinhar até acertar.(acertei)
numero = 4
chute = 0

while chute != numero:
    chute = int(input("Em qual número eu estou pensando? "))
    if chute > numero:
        print("Chute um número menor: ")
    elif chute < numero:
        print("Chute um número maior: ")
    else:
        print("Acertou!")

## pedir a senha até o usuário acertar. (acertei)
senha = "1234"
senha_dig = input("Digita sua senha: ")

while senha != senha_dig:
    print("SENHA INCORRETA!!")
    senha_dig = input("Digite novamente: ")

print("Entrou!!")

## Desafio extra: limite as tentativas a 3 e, se errar todas, mostre “Acesso bloqueado”. (fiz uma parte sozinho mas  final com 'else' que eu peguei a resposta)
senha = "1234"
senha_dig = input("Digita sua senha(3 tentativas): ")
tentativas = 3

while senha != senha_dig:
    tentativas -= 1
    if tentativas == 0:
        print("ACESSO BLOQUEADO!")
        break
    print(f"SENHA INCORRETA!! {tentativas} restantes")
    senha_dig = input("Digite novamente: ")
else:
    print("Entrou!!!")
   

