maquinas = ['Overloque', 'Reta', 'Colareti']
setores = ['Costura', 'Arremate', 'Corte', 'Produção', 'Administrativo']
costura = ['Rita Pimenta', 'Lourdes', 'Magda']
arremate = ['Luciana', 'Dayse', 'Cristina']
corte = ['Wiliton', 'Neide']
administrativo = ['Elaine']
producao = ['Marcus', 'Arthur']

operCosturaSaia = {
    'lateral':1.07,
    'elastCos':1.1,
    'bainha':1.01
}
def cadprod(funcionaria, maquina=0, operacao):
    print(f'Funcionária: {funcionaria}')
    if maquina != 0:
        print(f'Máquina: {maquina}')
    print(f'Operacao: {operacao}')
    for horaDia in range(8, 18):
        if horaDia == 13:
            continue
        else:
            qtdProduzida = input(str(horaDia)+':00 ==> ')
            totalProduzido += qtdProduzida
            horaDia += 1


# mostrando as horas que pego as produções
for horaDia in range(8, 18):
    if horaDia == 13:
        continue
    else:
        print(str(horaDia)+':00')
        horaDia += 1