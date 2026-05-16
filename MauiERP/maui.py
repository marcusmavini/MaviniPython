import customtkinter as ctk
import math as math

ctk.set_appearance_mode('Dark') # Janela em DarkMode
ctk.set_default_color_theme('blue')

root = ctk.CTk()

class AppMaui(ctk.CTk):
    def __init__(self):
        ctk.CTk.__init__(self)


root.title("Maui ERP")
root.geometry("500x500")


#titulo = ctk.label(text="Maui ERP") #Título Princial
#titulo.pack()

root.mainloop()


maquinas = ['Overloque', 'Reta', 'Colareti']
setores = ['Costura', 'Arremate', 'Corte', 'Produção', 'Administrativo']
costura = ['Rita Pimenta', 'Lourdes', 'Magda']
arremate = ['Luciana', 'Dayse', 'Cristina']
corte = ['Wiliton', 'Neide']
administrativo = ['Elaine']
producao = ['Marcus', 'Arthur']

operTimeCosturaSaia = {
    'lateral':1.07,
    'elastCos':1.1,
    'bainha':1.01
}

operCosturaSaia = ['Lateral', 'Elastico Cós', 'Bainha']


def cadprod(funcionaria, maquina='', opera='',operTime=0.0):
    # Cadastrar a produção de uma funcionária
    print(f'Funcionária: {funcionaria}')
    if maquina != 0:
        print(f'Máquina: {maquina}')
    print(f'Operação: {opera}')
    total = 0
    for horaDia in range(8, 18):
        if horaDia == 13:
            continue
        else:
            qtdProduzida = eval(input(f'{horaDia}:00 ==> '))
            total += qtdProduzida
            horaDia += 1
    print(f'O total produzido foi: {total}')
    tempoTrab = operTime * total
    print(f'Tempo trabalhado: {tempoTrab:.2f}')
    return tempoTrab

def eficiencia(funcionaria='',minSem=0):
    tempoTrab = cadprod(costura[2], maquinas[1], operCosturaSaia[0], operTimeCosturaSaia['lateral'])
    minSem = 2400
    calcEfSaia = (tempoTrab / minSem) * 100
    print(f'A Eficiência da funcionária {funcionaria} foi de {math.ceil(calcEfSaia)}%')

eficiencia(costura[2])
#cadprod(costura[2], maquinas[1], operCosturaSaia[0], operTimeCosturaSaia['lateral'])