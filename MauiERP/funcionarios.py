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

        # Construção da Frame principal
        self.janela = ctk.CTkFrame(self)
        self.janela.pack(fill='x', side='top')

        self.entrada_nome = ctk.CTkEntry(self.janela, placeholder_text="Nome", width=200, )
        self.entrada_nome.pack(pady=(10), padx=(10,10), side='left')

        self.selecionar_setores = ctk.CTkOptionMenu(self.janela, values=self.setores)
        self.selecionar_setores.pack(pady=(10), padx=(0,10), side='left')

        self.btn_s_setor = ctk.CTkButton(self.janela, text=">>", fg_color='grey', hover_color='darkgray', width=30, command=self.setorFuncao)
        self.btn_s_setor.pack(pady=(10), padx=(0,10), side='left')

        self.selecionar_funcao = ctk.CTkOptionMenu(self.janela, values=[], state='disabled')
        self.selecionar_funcao.pack(pady=(10), padx=(0,10), side='left')

        self.btn_cadastrar = ctk.CTkButton(self.janela, text="Cadastrar", fg_color='green', hover_color='darkgreen')
        self.btn_cadastrar.pack(pady=(10), padx=(0,10), side='left')


    def setorFuncao(self):
        setor = self.selecionar_setores.get()
        funcoes = self.funcoes[setor]

        self.selecionar_funcao.configure(values=funcoes, state='normal')
        self.selecionar_funcao.set(funcoes[0])




root = Funcionarios()
root.mainloop()
