# Este é um programa que tem uma lista simples de estoque e tem a opção de mostrar a lista e adicionar mais um item na lista

app = True
estoque = {
        'pelHigienico': 0,
        'Iinterfolha': 0,
    }
while app:
    def mostrar_itens():
        for itens in estoque:
            print(f'>> {itens} = {estoque[itens]}')

    def adicionar_item():
        print('Qual item deseja adicionar?\n')
        item = input('')
        print('Qual a quantidade?\n')
        quantidade = eval(input(''))
        estoque[item] = quantidade
        print(f'{item} adicionado com sucesso!')

    print('=====ESTOQUE MAUI=====')
    print('(1) Mostrar Itens\n(2) Adicionar Item\n(0) Sair')
    escolha = input('')
    if escolha == '1':
        mostrar_itens()
    elif escolha == '2':
        adicionar_item()
    else:
        app = False
else:
    print('===Fim===')
