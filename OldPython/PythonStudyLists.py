frutas = ["Banana","Uva","Maçã","Uva","Pêra","Abacaxi","Uva","Abacaxi"]
print("Esta é sua lista de frutas:")

for i in frutas:
    if i == "Uva":
        i = i + " Verde"
        print("> " + i)
    else:
        print("> " + i)
print("------------")

## Adicionando apenas uma fruta e msotrando a nova lista
novaFruta = input("Adicione uma nova fruta: ")
frutas.append(novaFruta)
quant = len(frutas)
print("Esta é sua nova lista de frutas: ")
print(f"Com {quant} itens")
print("------------")
for i in frutas:
    print("> " + i)
print("------------")

## Adicionando mais frutas na lista
maisFrutas = True
while maisFrutas == True:
    addFrutas = input("Quer adicionar mais uma fruta?(s/n) ")
    if addFrutas == "s":
        novaFruta = input("Digite a nova fruta: ")
        frutas.append(novaFruta)
    else:
        maisFrutas = not True
else:
    quant = len(frutas)
    print("Esta é sua nova lista de frutas: ")
    print(f"Com {quant} itens")
    print("------------")
    for i in frutas:
        print("> " + i)
    print("------------")

## Colocando em ordem alfabética
alfa = input("Quer que eu coloque em ordem alfabética?(s/n) ")
if alfa == "s":
    frutas.sort()
    print("Esta é sua nova lista de frutas: ")
    print(f"Com {quant} itens")
    print("------------")
    for i in frutas:
        print("> " + i)
    print("------------")
    print("Boas compras!")
else:
    print("Esta é sua lista de frutas: ")
    print(f"Com {quant} itens")
    print("------------")
    for i in frutas:
        print("> " + i)
    print("------------")
    print("Boas compras!")