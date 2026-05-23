from textwrap import fill

import customtkinter as ctk
ctk.set_appearance_mode("Dark") # Janela em DarkMode
ctk.set_default_color_theme("blue")

class Funcionarios(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Cadastro de Funcionários")
        self.geometry("600x600")

        self.setores = ['Administrativo', 'Produção', 'Costura', 'Arremate', 'Corte']
        self.funcoes = {
            "Administrativo": ['Auxiliar Administrativo'],
            "Produção": ['Chefe Operacional', 'Auxiliar de Produção'],
            "Costura": ['Costureira'],
            "Arremate": ['Arrematadeira', 'Passadeira', 'Revisora'],
            "Corte": ['Cortador', 'Auxiliar de Corte']
        }

        self.headers = ["Nome", "Setor", "Função"]

        self.data = [
            ["Rita", "Costura", "Costureira"],
            ["Luciana", "Arremate", "Arermatadeira"],
            # Add more rows as needed
        ]

        # Construção da Frame principal
        self.janela = ctk.CTkFrame(self)
        self.janela.pack(fill='x', side='top')

        self.trabalho = ctk.CTkFrame(self, fg_color='black')
        self.trabalho.pack(fill='x', side='top')

        self.entrada_nome = ctk.CTkEntry(self.janela, placeholder_text="Nome", width=200)
        self.entrada_nome.pack(pady=(10), padx=(10,10), side='left')

        self.selecionar_setores = ctk.CTkOptionMenu(self.janela, values=self.setores)
        self.selecionar_setores.pack(pady=(10), padx=(0,10), side='left')

        self.btn_s_setor = ctk.CTkButton(self.janela, text=">>", fg_color='grey', hover_color='darkgray', width=30, command=self.setorFuncao)
        self.btn_s_setor.pack(pady=(10), padx=(0,10), side='left')

        self.selecionar_funcao = ctk.CTkOptionMenu(self.janela, values=[], state='disabled')
        self.selecionar_funcao.pack(pady=(10), padx=(0,10), side='left')

        self.btn_cadastrar = ctk.CTkButton(self.janela, text="Cadastrar", fg_color='green', hover_color='darkgreen', command=self.cadastrar)
        self.btn_cadastrar.pack(pady=(10), padx=(0,10), side='left')

    def atualizar_tabela(self):
        dados = self.data
        for col, header in enumerate(self.headers):
            label = ctk.CTkLabel(self.trabalho, text=header, font=("Arial", 12, "bold"))
            label.pack(pady=(10), padx=(0,10), side='left')

        widths = [100, 50, 200]

        for row, row_data in enumerate(dados, start=1):
            for col, value in enumerate(row_data):
                self.entry = ctk.CTkEntry(self.trabalho, width=widths[col])
                self.entry.insert(ctk.END, value)
                self.entry.pack(padx=(0,10), side='left')


    def setorFuncao(self):
        setor = self.selecionar_setores.get()
        funcoes = self.funcoes[setor]

        self.selecionar_funcao.configure(values=funcoes, state='normal')
        self.selecionar_funcao.set(funcoes[0])

    def cadastrar(self):
        nome = self.entrada_nome.get()
        setor = self.selecionar_setores.get()
        funcao = self.selecionar_funcao.get()
        dados = [nome, setor, funcao]
        self.data.append(dados)
        print(self.data)
        self.atualizar_tabela()


root = Funcionarios()
root.mainloop()
