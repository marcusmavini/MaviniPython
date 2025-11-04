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