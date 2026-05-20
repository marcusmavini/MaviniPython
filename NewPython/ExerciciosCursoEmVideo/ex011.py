# largura e altura de uma parede e calcular área e quantidade de tinta para pintar. cada litro pinta 2m²
"""
Entrada: Largura e Altura da parede
Saída: Área da parede e quantidade de tinta para pitá-la
"""
print('===DESAFIO 011===')

l = float(input('Qual a largura da parede em metros: '))
a = float(input('Qual a altura da parede em metros: '))

area = l * a
quantTinta = area / 2

print(f'Para pintar a parede irá precisar de {quantTinta:.1f} litros de tinta')

escolha = input('Mais detalhes? (s/n)')

if escolha == 's':
    print(f'Largura >> {l}m\nAltura >> {a}m\nÁrea >> {area}m²')
else:
    print('Fim')
