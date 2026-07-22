import customtkinter as ctk
import math
import emoji

class Operacao:
    def __init__(self, operacao):
        self.op = operacao

    def checkOP(self, escolha_operacao):
        if escolha_operacao not in self.op:
            print('A operação não está na lista!')
            return True
        else:
            return False

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Cria a janela principal
app = ctk.CTk()
app.geometry("690x300")
app.title("App Maui")

op = Operacao(
    {
        #--Saia--
        #Overloque
        'lateral saia':1.07,
        'elastico cos':0.97,
        #Reta
        'etiqueta saia':0.37,
        'fita saia':0.64,
        'fechar elastico':0.18,
        #Colarete
        'rebater':0.55,
        'bainha':0.52,
        #--Top--
        #Overloque
        'lateral top':0.71,
        'lateral forro':0.52,
        'fechar em cima':0.9,
        'elastico busto':1,
        'rodar total':0.87,
        #Reta
        'elastico busto reta':0.84,
        'fechar buraco':0.6,
        'etiqueta top':0.44,
        'fita top':0.79,
        'lateral reta':0.95,
        'fechar em cima reta':1.22,

        # =======ARREMATE========
        #--Saia--
        'revisao saia':0.35,
        'ferro saia':0.51,
        'arremate saia':1.84,
        'elastico':0.11,
        #--Top--
        'revisao top':0.3,
        'ferro top':0.23,
        'arremate top':0.84
    }
)

def setOP():
    modelo = escolha_modelo.get()
    maquina= escolha_maquina.get()

    if modelo == 'Saia':
        if maquina == 'Overloque':
            escolha_operacao.configure(values=['Lateral Saia', 'Elastico Cos'])
            escolha_operacao.set('Lateral Saia')
        elif maquina == 'Reta':
            escolha_operacao.configure(values=['Etiqueta Saia', 'Fita Saia', 'Fechar Elastico'])
            escolha_operacao.set('Etiqueta Saia')
        elif maquina == 'Colarete':
            escolha_operacao.configure(values=['Rebater', 'Bainha'])
            escolha_operacao.set('Rebater')
        elif maquina == 'Arremate':
            escolha_operacao.configure(values=['Revisao Saia', 'Ferro Saia', 'Arremate Saia', 'Elastico'])
            escolha_operacao.set('Revisao Saia')
    elif modelo == 'Top':
        if maquina == 'Overloque':
            escolha_operacao.configure(values=['Lateral Top', 'Lateral Forro', 'Fechar em Cima', 'Elastico Busto', 'Rodar Total'])
            escolha_operacao.set('Lateral Top')
        elif maquina == 'Reta':
            escolha_operacao.configure(values=['Etiqueta Top', 'Fita Top', 'Fechar Buraco', 'Elastico Busto Reta', 'Lateral Reta', 'Fechar em Cima Reta'])
            escolha_operacao.set('Etiqueta Top') 
        elif maquina == 'Colarete':
            escolha_operacao.configure(values=['Não tem'])
            escolha_operacao.set('Não tem')
        elif maquina == 'Arremate':
            escolha_operacao.configure(values=['Revisao Top', 'Ferro Top', 'Arremate Top', 'Elastico'])
            escolha_operacao.set('Revisao Top')
    elif modelo == 'Blusa':
        escolha_operacao.configure(values=['Em construção..'])
        escolha_operacao.set('Em construção..')

#-------------- FRAME MENU SUPERIOR ----------------
  
#-------------- FRAME BARRA DADOS ENTRADA ----------------
emoji.emojize(':thumbs_up:')
fr_barra_topo = ctk.CTkFrame(app)
fr_barra_topo.pack(fill='x', pady=(0,10))

nome_funcionaria = ctk.CTkEntry(fr_barra_topo, placeholder_text='Nome')
nome_funcionaria.pack(padx=5, side='left')

escolha_modelo = ctk.CTkOptionMenu(fr_barra_topo, values=['Saia', 'Top', 'Blusa'], width=100)
escolha_modelo.pack(padx=5, side='left')

escolha_maquina = ctk.CTkOptionMenu(fr_barra_topo, width=100, values=['Overloque', 'Reta', 'Colarete', 'Arremate'])
escolha_maquina.pack(padx=5, side='left')

confirma_mod_maq = ctk.CTkButton(fr_barra_topo, text='>>', width=50, command=setOP)
confirma_mod_maq.pack(padx=5, side='left')

escolha_operacao = ctk.CTkOptionMenu(fr_barra_topo, values=['Lateral Saia', 'Elastico Cos', 'Etiqueta Saia'])
escolha_operacao.pack(padx=5, side='left')


qtd_adicionados = ctk.CTkLabel(fr_barra_topo, text=f'{emoji.emojize(':large_blue_diamond:')} 0')
qtd_adicionados.pack(padx=5, side='left')
#-------------------------------------------------
#------------ FRAME BARRA PRODUÇÕES --------------
fr_barra_prods = ctk.CTkFrame(app)
fr_barra_prods.pack(fill='x')
#-------------------------------------------------
fr_hora8 = ctk.CTkFrame(fr_barra_prods)
fr_hora8.pack(padx=2, side='left')
                         
hora_title8 = ctk.CTkLabel(fr_hora8, text='8:00')
hora_title8.pack(padx=2)

prod_campo8 = ctk.CTkEntry(fr_hora8, width=50)
prod_campo8.pack()
    #-------------------------------------------------
fr_hora9 = ctk.CTkFrame(fr_barra_prods)
fr_hora9.pack(padx=2, side='left')
                            
hora_title9 = ctk.CTkLabel(fr_hora9, text='9:00')
hora_title9.pack(padx=2)

prod_campo9 = ctk.CTkEntry(fr_hora9, width=50)
prod_campo9.pack()
    #-------------------------------------------------
fr_hora10 = ctk.CTkFrame(fr_barra_prods)
fr_hora10.pack(padx=2, side='left')
                            
hora_title10 = ctk.CTkLabel(fr_hora10, text='10:00')
hora_title10.pack(padx=2)

prod_campo10 = ctk.CTkEntry(fr_hora10, width=50)
prod_campo10.pack()
    #-------------------------------------------------
fr_hora11 = ctk.CTkFrame(fr_barra_prods)
fr_hora11.pack(padx=2, side='left')
                            
hora_title11 = ctk.CTkLabel(fr_hora11, text='11:00')
hora_title11.pack(padx=2)

prod_campo11 = ctk.CTkEntry(fr_hora11, width=50)
prod_campo11.pack()
    #-------------------------------------------------
fr_hora12 = ctk.CTkFrame(fr_barra_prods)
fr_hora12.pack(padx=2, side='left')
                            
hora_title12 = ctk.CTkLabel(fr_hora12, text='12:00')
hora_title12.pack(padx=2)

prod_campo12 = ctk.CTkEntry(fr_hora12, width=50)
prod_campo12.pack()
    #-------------------------------------------------
fr_hora14 = ctk.CTkFrame(fr_barra_prods)
fr_hora14.pack(padx=2, side='left')
                            
hora_title14 = ctk.CTkLabel(fr_hora14, text='14:00')
hora_title14.pack(padx=2)

prod_campo14 = ctk.CTkEntry(fr_hora14, width=50)
prod_campo14.pack()
    #-------------------------------------------------
fr_hora15 = ctk.CTkFrame(fr_barra_prods)
fr_hora15.pack(padx=2, side='left')
                            
hora_title15 = ctk.CTkLabel(fr_hora15, text='15:00')
hora_title15.pack(padx=2)

prod_campo15 = ctk.CTkEntry(fr_hora15, width=50)
prod_campo15.pack()
#-------------------------------------------------
fr_hora16 = ctk.CTkFrame(fr_barra_prods)
fr_hora16.pack(padx=2, side='left')
                            
hora_title16 = ctk.CTkLabel(fr_hora16, text='16:00')
hora_title16.pack(padx=2)

prod_campo16 = ctk.CTkEntry(fr_hora16, width=50)
prod_campo16.pack()
#-------------------------------------------------
fr_hora17 = ctk.CTkFrame(fr_barra_prods)
fr_hora17.pack(padx=2, side='left')
                           
hora_title17 = ctk.CTkLabel(fr_hora17, text='17:00')
hora_title17.pack(padx=2)

prod_campo17 = ctk.CTkEntry(fr_hora17, width=50)
prod_campo17.pack()
#-------------------------------------------------
resultado = ctk.CTkLabel(app, text='O resultado vai aparecer aqui!', font=('Verdana', 20))
resultado.pack(pady=10)
#----------------------TABELA COM RESULTADOS---------------------------


def somarProd():
    getCampo8 = prod_campo8.get()
    getCampo9 = prod_campo9.get()
    getCampo10 = prod_campo10.get()
    getCampo11 = prod_campo11.get()
    getCampo12 = prod_campo12.get()
    getCampo14 = prod_campo14.get()
    getCampo15 = prod_campo15.get()
    getCampo16 = prod_campo16.get()
    getCampo17 = prod_campo17.get()
    lista = [getCampo8, getCampo9, getCampo10, getCampo11, getCampo12, getCampo14, getCampo15, getCampo16, getCampo17]

    for i in lista:
        posicao = lista.index(i)
        if i == '':
            lista[posicao] = 0
        else:
            lista[posicao] = float(lista[posicao])
            
    '''
    campo8 = float(getCampo8)
    campo9 = float(getCampo9)
    campo10 = float(getCampo10)
    campo11 = float(getCampo11)
    campo12 = float(getCampo12)
    campo14 = float(getCampo14)
    campo15 = float(getCampo15)
    campo16 = float(getCampo16)
    campo17 = float(getCampo17)
    '''
    #soma = campo8 + campo9 + campo10 + campo11 + campo12 + campo14 + campo15 + campo16 + campo17  
    soma = sum(lista)
    return soma
    #operacao = soma * 1.07
    #resultado.configure(text=f'> Total Produzido: {soma}\n> Minutos Produzidos: {operacao:.2f}')
entradas = []
def minProd_eficiencia():
    totalProd = somarProd()
    tempoOP = op.op[escolha_operacao.get().lower()]
    
    minutosProduzidos = totalProd * tempoOP
    eficiencia = (minutosProduzidos / 480)*100

    nomeFunc = nome_funcionaria.get()
    getMaquina = escolha_maquina.get()
    getModelo = escolha_modelo.get()
    getOP = escolha_operacao.get()

    saida = {'Nome':nomeFunc, 'Modelo':getModelo, 'Máquina':getMaquina, 'Operação':getOP, 'Total Produzido':totalProd, 'Tempo Operação':tempoOP, 'Minutos Produzidos':minutosProduzidos, 'Eficiência':eficiencia}
    entradas.append(saida)
    #print(entradas)
    adicionados = len(entradas)
    resultado.configure(text=f'> Total Produzido: {totalProd}\n> Minutos Produzidos: {minutosProduzidos:.2f}\n> Eficiência: {math.ceil(eficiencia)}%')
    qtd_adicionados.configure(text=f'{emoji.emojize(':large_blue_diamond:')} {adicionados}')

def mostrarEntradas():
    for entrada in entradas:
        fr_barra_entradas = ctk.CTkFrame(app)
        fr_barra_entradas.pack(pady=10, fill='x')
        #------------------
        fr_title_entrada = ctk.CTkFrame(fr_barra_entradas)
        fr_title_entrada.pack(fill='x')

        ent_nome_funcionaria = ctk.CTkLabel(fr_title_entrada, text=f'{entrada['Nome']}')
        ent_nome_funcionaria.pack(side='left', padx=(10, 25))

        ent_operacao = ctk.CTkLabel(fr_title_entrada, text=f'{entrada['Operação'].upper()} ({entrada['Tempo Operação']})')
        ent_operacao.pack(side='left', padx=10)

        ent_maquina = ctk.CTkLabel(fr_title_entrada, text=f'{entrada['Máquina'].upper()}')
        ent_maquina.pack(side='left', padx=10)

        if entrada['Modelo'] == 'Saia':
            ent_modelo = ctk.CTkLabel(fr_title_entrada, text=f'{entrada['Modelo'].upper()}', fg_color='blue')
            ent_modelo.pack(side='left', padx=10, ipadx=10)
        elif entrada['Modelo'] == 'Top':
            ent_modelo = ctk.CTkLabel(fr_title_entrada, text=f'{entrada['Modelo'].upper()}', fg_color='black')
            ent_modelo.pack(side='left', padx=10, ipadx=10)
        #------------------
        ent_totalProduzido = ctk.CTkLabel(fr_barra_entradas, text=f'Total Produzido: {entrada['Total Produzido']:.2f}')
        ent_totalProduzido.pack(side='left', padx=10)

        ent_minutosProduzidos = ctk.CTkLabel(fr_barra_entradas, text=f'Minutos Produzidos: {entrada['Minutos Produzidos']:.2f}')
        ent_minutosProduzidos.pack(side='left', padx=10)

        ent_efc = ctk.CTkLabel(fr_barra_entradas, text=f'Eficiência: {math.ceil(entrada['Eficiência'])}%')
        ent_efc.pack(side='left', padx=10)


btn_calcular = ctk.CTkButton(fr_barra_prods, text='Calcular', command=minProd_eficiencia, width=80, fg_color='green', hover_color='darkgreen')
btn_calcular.pack(padx=5, side='left')

#btn_reset = ctk.CTkButton(fr_barra_prods, text='Reset', width=70, fg_color='#ED7014', hover_color='#8D4004')
#btn_reset.pack(padx=5, side='left')

btn_relatorio = ctk.CTkButton(fr_barra_prods, text='Relatório', width=80, command=mostrarEntradas, fg_color='#ED7014', hover_color='#8D4004')
btn_relatorio.pack(padx=5, side='left')


app.mainloop()
