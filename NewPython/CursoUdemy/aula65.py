nome = input('Digite seu nome: ')
contador = 0
nova_string = ''
while contador < len(nome):
    nova_string += f'*{nome[contador]}'
    contador += 1
else:
    print(nova_string)