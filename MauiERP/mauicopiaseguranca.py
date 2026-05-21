import customtkinter as ctk
import math as math
import time

ctk.set_appearance_mode("Dark") # Janela em DarkMode
ctk.set_default_color_theme("blue")

class AppMaui(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Maui ERP')
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

    # ========> POSICIONANDO OS ELEMENTOS <========
    def construir_abalateral(self):
        self.titulo = ctk.CTkLabel(self.barra_lateral, text='Maui ERP', font=ctk.CTkFont(size=24, weight='bold'))
        self.titulo.pack(pady=(30,5), padx=(20,20))

        self.subtitulo = ctk.CTkLabel(self.barra_lateral, text='')
        self.subtitulo.pack(pady=(0, 5))

        # ==========> ESCOLHA DE SETORES <==========
        # ====> OPERACIONAL <====
        self.subtitulo_operacional = ctk.CTkLabel(self.barra_lateral, text='Operacional', font=ctk.CTkFont(size=15))
        self.subtitulo_operacional.pack(pady=(30, 5), padx=(10, 10))

        self.btn_producoes = ctk.CTkButton(self.barra_lateral, text='Produções', command=self.ir_para_dashboard)
        self.btn_producoes.pack(pady=(0,10), padx=(10,10))

        self.btn_entregas = ctk.CTkButton(self.barra_lateral, text='Entregas', command=self.ir_para_dashboard)
        self.btn_entregas.pack(pady=(0, 10), padx=(10, 10))

        self.btn_eficiencia = ctk.CTkButton(self.barra_lateral, text='Eficiência', command=self.ir_para_dashboard)
        self.btn_eficiencia.pack(pady=(0, 10), padx=(10, 10))

        self.btn_ferramentas = ctk.CTkButton(self.barra_lateral, text='Ferramentas', command=self.ir_para_dashboard)
        self.btn_ferramentas.pack(pady=(0, 10), padx=(10, 10))

        # ====> ADMINISTRATIVO <====
        self.subtitulo_administrativo = ctk.CTkLabel(self.barra_lateral, text='Administrativo', font=ctk.CTkFont(size=15))
        self.subtitulo_administrativo.pack(pady=(30, 5), padx=(10, 10))

        self.btn_funcionarios = ctk.CTkButton(self.barra_lateral, text='Funcionários', command=self.ir_para_dashboard)
        self.btn_funcionarios.pack(pady=(0, 10), padx=(10, 10))

        self.btn_financeiro = ctk.CTkButton(self.barra_lateral, text='Financeiro', command=self.ir_para_dashboard)
        self.btn_financeiro.pack(pady=(0, 10), padx=(10, 10))

        self.switch_mododark = ctk.CTkSwitch(self.barra_lateral, text='Switch Dark', command=self.mudar_modo_dark)
        self.switch_mododark.pack(pady=(30, 10), padx=(10,10), side='bottom')
        self.switch_mododark.select()

    def construir_abaperfil(self):
        self.aba_perfil = self.janela_abas.tab('Perfil')
        self.campo_nome = ctk.CTkEntry(self.aba_perfil, placeholder_text='Digite o seu nome', width=300)
        self.campo_nome.pack(pady=(20, 20), padx=(10,10))

        self.nivel_usuario = ctk.IntVar(value=0)

        # Escolher usuário
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
        self.botao_salvarperfil = ctk.CTkButton(self.aba_perfil, text='Salvar Perfil', fg_color='green', hover_color='darkgreen', command=self.salvar_perfil)
        self.botao_salvarperfil.pack(pady=(20,20))

    def construir_abapreferencias(self):
        self.aba_preferencias = self.janela_abas.tab('Preferências')

        # Menu select com opções
        self.label_idiomas = ctk.CTkLabel(self.aba_preferencias, text='Selecione o Idioma')
        self.label_idiomas.pack(pady=(20,5))
        self.menu_idiomas = ctk.CTkOptionMenu(self.aba_preferencias, values=['Português', 'Inglês', 'Espanhol'])
        self.menu_idiomas.pack()

        # Slider de volume
        self.label_volume = ctk.CTkLabel(self.aba_preferencias, text='Volume do Sistema')
        self.label_volume.pack(pady=(20,5))
        self.slider_volume = ctk.CTkSlider(self.aba_preferencias, from_=0, to=100, command=self.atualizar_volume)
        self.slider_volume.pack()
        self.slider_volume.set(50) # Deixa o valor padrão em 50
        self.label_valor_volume = ctk.CTkLabel(self.aba_preferencias, text='50%')
        self.label_valor_volume.pack()

    def construir_abasistema(self):
        self.aba_sistema = self.janela_abas.tab('Dashboard')

        self.label_carregamento = ctk.CTkLabel(self.aba_sistema, text='Testar Carregamento do Sistema', font=ctk.CTkFont(size=16))
        self.label_carregamento.pack()

        self.barra_progresso = ctk.CTkProgressBar(self.aba_sistema, width=400)
        self.barra_progresso.pack(pady=(10,10))
        self.barra_progresso.set(0)

        self.botao_progresso = ctk.CTkButton(self.aba_sistema, text='Iniciar Carregamento', command=self.carregar)
        self.botao_progresso.pack(pady=(10,10))

    # ========> AÇÕES <========
    def ir_para_dashboard(self):
        self.janela_abas.set('Dashboard') #Muda de janela

    def mudar_modo_dark(self):
        if self.switch_mododark.get() == 1:
            ctk.set_appearance_mode("Dark")
        else:
            ctk.set_appearance_mode("System")

    def salvar_perfil(self):
        nome = self.campo_nome.get()
        if self.nivel_usuario.get() == 2:
            nivel = 'Admin'
        else:
            nivel = 'Básico'
        receber_notificacoes = self.checkbox_notificacoes.get()

        print(f'Nome: {nome}\nNível: {nivel}\nReceber Notificações: {receber_notificacoes}')

        self.titulo.configure(text=f"{nome} ERP") # Altera um texto
        self.subtitulo.configure(text=nivel)

    def atualizar_volume(self, novo_valor_volume):
        self.label_valor_volume.configure(text=f'{int(novo_valor_volume)}%')

    def carregar(self):
        for i in range(100):
            #executar uma tarefa que pode demorar
            time.sleep(0.1)
            self.barra_progresso.set((i + 1)/100)
            self.update()


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