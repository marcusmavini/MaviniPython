# Preço de um produto e mostrar com 5% de de desconto
"""
Entrada: preço do produto
Saída: Preço do produto com desconto
"""
print('===DESAFIO 012===')

produto = input('Digite o nome do produto: ')
precoProduto = float(input('Digite o valor do produto: '))

desconto5 = precoProduto - (precoProduto *0.05)
print('='*20)
print(f'Produto: {produto}\nValor: R${precoProduto:.2f}\nDesconto: R${precoProduto*0.05:.2f} (5%)\nVALOR TOTAL: R${desconto5:.2f}')