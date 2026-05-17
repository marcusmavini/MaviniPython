import customtkinter as ctk
import math as math

ctk.set_appearance_mode('Dark') # Janela em DarkMode
ctk.set_default_color_theme('blue')

class AppMaui(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Maui')
        self.geometry('900x600')

        # Divisão da tela
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Parte lateral
        self.barra_lateral = ctk.CTkFrame(self, width=200)
        self.barra_lateral.grid(row=0, column=0, sticky='NSEW')

        # parte principal
        self.janela_abas = ctk.CTkTabview(self, width=400)
        self.janela_abas.grid(row=0, column=1, sticky='NSEW', padx=10)

        self.janela_abas.add('Perfil')
        self.janela_abas.add('Preferências')
        self.janela_abas.add('Dashboard')

        self.construir_abalateral()
        self.construir_abaperfil()
        self.construir_abapreferencias()
        self.construir_abasistema()

    def construir_abalateral(self):
        self.titulo = ctk.CTkLabel(self.barra_lateral, text='Maui ERP', font=ctk.CTkFont(size=24, weight='bold'))
        self.titulo.pack(pady=(30, 10), padx=(20,20))

        self.botao_principal = ctk.CTkButton(self.barra_lateral, text='Botão')
        self.botao_principal.pack(pady=(30, 10), padx=(10,10))

        self.switch_mododark = ctk.CTkSwitch(self.barra_lateral, text='Switch Dark')
        self.switch_mododark.pack(pady=(30, 10), padx=(10,10), side='bottom')

    def construir_abaperfil(self):
        self.aba_perfil = self.janela_abas.tab('Perfil')
        self.campo_nome = ctk.CTkEntry(self.aba_perfil, placeholder_text='Digite o seu nome', width=300)
        self.campo_nome.pack(pady=(20, 20), padx=(10,10))

        self.nivel_usuario = ctk.IntVar(value=0)

        self.radio_label = ctk.CTkLabel(self.aba_perfil, text='Nível Usuário')
        self.radio_basico = ctk.CTkRadioButton(self.aba_perfil, text='Básico', variable=self.nivel_usuario, value=1)
        self.radio_admin = ctk.CTkRadioButton(self.aba_perfil, text='Admin', variable=self.nivel_usuario, value=2)

        self.radio_label.pack()
        self.radio_basico.pack()
        self.radio_admin.pack()

        # Checkbox notificações
        self.checkbox_notificacoes = ctk.CTkCheckBox(self.aba_perfil, text='Receber notificações por e-mail')
        self.checkbox_notificacoes.pack(pady=(20,20))

        # Salvar perfil
        self.botao_salvarperfil = ctk.CTkButton(self.aba_perfil, text='Salvar Perfil', fg_color='green', hover_color='darkgreen')
        self.botao_salvarperfil.pack(pady=(20,20))

    def construir_abapreferencias(self):
        pass

    def construir_abasistema(self):
        pass

root = AppMaui()
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