import customtkinter as ctk

# =========================================================
# CONFIGURAÇÕES INICIAIS
# =========================================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Projeto HERO")
app.geometry("1400x800")

# =========================================================
# DADOS DO JOGADOR
# =========================================================

jogador = {
    "nome": "Lionel",
    "origem": "Alienígena",
    "classe": "Olímpico",
    "nivel": 1,
    "xp": 0,
    "dinheiro": 500,

    "atributos": {
        "PF": 10,
        "AGI": 8,
        "VIT": 12,
        "INT": 5,
        "VON": 6,
        "PRE": 4
    },

    "sociais": {
        "REP": 0,
        "INF": 0,
        "NOT": 0
    }
}

# =========================================================
# MISSÕES
# =========================================================

missoes = [
    {
        "nome": "Patrulha Urbana",
        "descricao": "Derrote criminosos no centro da cidade.",
        "xp": 100,
        "dinheiro": 80,
        "dificuldade": "Fácil"
    },

    {
        "nome": "Anomalia Energética",
        "descricao": "Investigue distorções próximas ao setor industrial.",
        "xp": 250,
        "dinheiro": 180,
        "dificuldade": "Média"
    },

    {
        "nome": "Ameaça Titânica",
        "descricao": "Enfrente uma criatura modificada fora de controle.",
        "xp": 500,
        "dinheiro": 350,
        "dificuldade": "Difícil"
    }
]

# =========================================================
# FUNÇÕES
# =========================================================


def limpar_main():
    for widget in main_frame.winfo_children():
        widget.destroy()


# =========================================================
# TELA HOME
# =========================================================


def abrir_home():
    limpar_main()

    titulo = ctk.CTkLabel(
        main_frame,
        text="HOME",
        font=("Arial", 28, "bold")
    )
    titulo.pack(pady=20)

    texto = ctk.CTkLabel(
        main_frame,
        text="Bem-vindo ao sistema da Agência HERO.",
        font=("Arial", 18)
    )
    texto.pack(pady=10)


# =========================================================
# TELA MISSÕES
# =========================================================


def abrir_missoes():
    limpar_main()

    titulo = ctk.CTkLabel(
        main_frame,
        text="MISSÕES",
        font=("Arial", 28, "bold")
    )
    titulo.pack(pady=20)

    for missao in missoes:

        card = ctk.CTkFrame(main_frame)
        card.pack(fill="x", padx=20, pady=10)

        nome = ctk.CTkLabel(
            card,
            text=missao["nome"],
            font=("Arial", 20, "bold")
        )
        nome.pack(anchor="w", padx=10, pady=5)

        descricao = ctk.CTkLabel(
            card,
            text=missao["descricao"]
        )
        descricao.pack(anchor="w", padx=10)

        recompensa = ctk.CTkLabel(
            card,
            text=f"XP: {missao['xp']} | Dinheiro: ${missao['dinheiro']}"
        )
        recompensa.pack(anchor="w", padx=10, pady=5)

        botao = ctk.CTkButton(
            card,
            text="Iniciar Missão"
        )
        botao.pack(padx=10, pady=10)


# =========================================================
# TELA PERFIL
# =========================================================


def abrir_perfil():
    limpar_main()

    titulo = ctk.CTkLabel(
        main_frame,
        text="PERFIL",
        font=("Arial", 28, "bold")
    )
    titulo.pack(pady=20)

    info = f"""
Nome: {jogador['nome']}
Origem: {jogador['origem']}
Classe: {jogador['classe']}
Nível: {jogador['nivel']}
XP: {jogador['xp']}
Dinheiro: ${jogador['dinheiro']}
    """

    dados = ctk.CTkLabel(
        main_frame,
        text=info,
        justify="left",
        font=("Arial", 18)
    )
    dados.pack(anchor="w", padx=20)

    subtitulo = ctk.CTkLabel(
        main_frame,
        text="ATRIBUTOS",
        font=("Arial", 22, "bold")
    )
    subtitulo.pack(anchor="w", padx=20, pady=20)

    for atributo, valor in jogador["atributos"].items():
        linha = ctk.CTkLabel(
            main_frame,
            text=f"{atributo}: {valor}",
            font=("Arial", 16)
        )
        linha.pack(anchor="w", padx=30)


# =========================================================
# HEADER
# =========================================================

header = ctk.CTkFrame(app, height=70)
header.pack(fill="x")

logo = ctk.CTkLabel(
    header,
    text="HERO",
    font=("Arial", 30, "bold")
)
logo.pack(side="left", padx=20)

menu_frame = ctk.CTkFrame(header, fg_color="transparent")
menu_frame.pack(side="right", padx=20)

btn_home = ctk.CTkButton(menu_frame, text="Home", command=abrir_home)
btn_home.pack(side="left", padx=5)

btn_loja = ctk.CTkButton(menu_frame, text="Loja")
btn_loja.pack(side="left", padx=5)

btn_eventos = ctk.CTkButton(menu_frame, text="Eventos")
btn_eventos.pack(side="left", padx=5)

btn_ranking = ctk.CTkButton(menu_frame, text="Ranking")
btn_ranking.pack(side="left", padx=5)

btn_avisos = ctk.CTkButton(menu_frame, text="Avisos")
btn_avisos.pack(side="left", padx=5)

btn_config = ctk.CTkButton(menu_frame, text="Config")
btn_config.pack(side="left", padx=5)

# =========================================================
# CONTAINER PRINCIPAL
# =========================================================

container = ctk.CTkFrame(app)
container.pack(fill="both", expand=True)

# =========================================================
# LATERAL ESQUERDA
# =========================================================

left_sidebar = ctk.CTkFrame(container, width=300)
left_sidebar.pack(side="left", fill="y", padx=5, pady=5)
left_sidebar.pack_propagate(False)

perfil_titulo = ctk.CTkLabel(
    left_sidebar,
    text=jogador["nome"],
    font=("Arial", 24, "bold")
)
perfil_titulo.pack(pady=15)

classe_label = ctk.CTkLabel(
    left_sidebar,
    text=f"{jogador['origem']} | {jogador['classe']}"
)
classe_label.pack()

# ATRIBUTOS

atributos_titulo = ctk.CTkLabel(
    left_sidebar,
    text="ATRIBUTOS",
    font=("Arial", 18, "bold")
)
atributos_titulo.pack(pady=15)

for atributo, valor in jogador["atributos"].items():
    label = ctk.CTkLabel(
        left_sidebar,
        text=f"{atributo}: {valor}"
    )
    label.pack(anchor="w", padx=20)

# SOCIAIS

sociais_titulo = ctk.CTkLabel(
    left_sidebar,
    text="SOCIAIS",
    font=("Arial", 18, "bold")
)
sociais_titulo.pack(pady=15)

for atributo, valor in jogador["sociais"].items():
    label = ctk.CTkLabel(
        left_sidebar,
        text=f"{atributo}: {valor}"
    )
    label.pack(anchor="w", padx=20)

# BOTÕES

btn_perfil = ctk.CTkButton(
    left_sidebar,
    text="Perfil",
    command=abrir_perfil
)
btn_perfil.pack(fill="x", padx=20, pady=5)

btn_habilidades = ctk.CTkButton(
    left_sidebar,
    text="Habilidades"
)
btn_habilidades.pack(fill="x", padx=20, pady=5)

btn_aprimoramentos = ctk.CTkButton(
    left_sidebar,
    text="Aprimoramentos"
)
btn_aprimoramentos.pack(fill="x", padx=20, pady=5)

# =========================================================
# MAIN
# =========================================================

main_frame = ctk.CTkFrame(container)
main_frame.pack(side="left", fill="both", expand=True, padx=5, pady=5)

# =========================================================
# LATERAL DIREITA
# =========================================================

right_sidebar = ctk.CTkFrame(container, width=250)
right_sidebar.pack(side="right", fill="y", padx=5, pady=5)
right_sidebar.pack_propagate(False)

menu_titulo = ctk.CTkLabel(
    right_sidebar,
    text="MENU",
    font=("Arial", 22, "bold")
)
menu_titulo.pack(pady=15)

btn_missoes = ctk.CTkButton(
    right_sidebar,
    text="Missões",
    command=abrir_missoes
)
btn_missoes.pack(fill="x", padx=20, pady=5)

btn_inventario = ctk.CTkButton(
    right_sidebar,
    text="Inventário"
)
btn_inventario.pack(fill="x", padx=20, pady=5)

btn_equipamento = ctk.CTkButton(
    right_sidebar,
    text="Equipamento"
)
btn_equipamento.pack(fill="x", padx=20, pady=5)

btn_chips = ctk.CTkButton(
    right_sidebar,
    text="Chips"
)
btn_chips.pack(fill="x", padx=20, pady=5)

# =========================================================
# RODAPÉ
# =========================================================

footer = ctk.CTkFrame(app, height=40)
footer.pack(fill="x")

footer_label = ctk.CTkLabel(
    footer,
    text="Projeto HERO © 2026"
)
footer_label.pack(pady=10)

# =========================================================
# INICIAR HOME
# =========================================================

abrir_home()

# =========================================================
# LOOP
# =========================================================

app.mainloop()