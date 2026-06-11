from classes import player
import math
import customtkinter as ctk

# =========================================================
# CONFIGURAÇÕES INICIAIS
# =========================================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Poder Absoluto")
app.geometry("720x580")

# =========================================================
# DADOS DO JOGADOR
# =========================================================

player1 = player.Player(
    'Lionel',
    'Humano',
    'Condutor',
    1,
    100,
    200,

    {
        'Strenght':15,
        'Agility':14,
        'Vitality':13,
        'Inteligence':12,
        'Will':11,
        'Presence':10
    },
    {
        'Health':200,
        'Max Health':1000,
        'Energy':500,
        'Max Energy':500,
        'Physical Damage':50,
        'Power':25,
        'Defense':300
    },
    {
        'Reputation':50,
        'Infamy':0,
        'Notoriety':20  
    }
)


def more_stats():
    title_more_stats = ctk.CTkLabel(
        app,
        text="Mais Informações",
        font=("Arial", 20, "bold")
    )
    title_more_stats.pack(pady=20)

    moreStats = f'''Vida: {player1.aspec['Health']}/{player1.aspec['Max Health']}
Energia: {player1.aspec['Energy']}/{player1.aspec['Max Energy']}
Dano Físico: {player1.aspec['Physical Damage']}'''

    more_stats = ctk.CTkLabel(app, text=moreStats, font=('Arial', 15))
    more_stats.pack(pady=(5,5))

def ganharxp(quant):
    player1.gainXP(quant)
    show_level.configure(text=f'NÍVEL: {player1.level}\n[XP]{player1.xp}/{player1.xpMax}')
    
show_level = ctk.CTkLabel(master=app, text=f'NÍVEL: {player1.level}\n[XP]{player1.xp}/{player1.xpMax}')
show_level.pack()
# =========================================================
# ATRIBUTOS
# =========================================================
title_screen_attr = ctk.CTkLabel(app, text='Atributos', font=('Arial', 20, 'bold'))
title_screen_attr.pack(pady=(5,0))
screen_attr = ctk.CTkLabel(app, text=f'''Força: {player1.attr['Strenght']}
Agilidade: {player1.attr['Agility']}
Vitalidade: {player1.attr['Vitality']}
[INT] {player1.attr['Inteligence']}
[VON] {player1.attr['Will']}
[PRE] {player1.attr['Presence']}''', font=('Arial', 15))
screen_attr.pack(pady=(0,10))
# =========================================================
# ATRIBUTOS SOCIAIS
# =========================================================
title_screen_socialattr = ctk.CTkLabel(app, text='Atributos Sociais', font=('Arial', 20, 'bold'))
title_screen_socialattr.pack()

screen_socialattr = ctk.CTkLabel(app, text=f'''[REP] {player1.sAttr['Reputation']}
[INF] {player1.sAttr['Infamy']}
[NOT] {player1.sAttr['Notoriety']}''', font=('Arial', 15))
screen_socialattr.pack()
# =========================================================
# A
# =========================================================

btn_more_stats = ctk.CTkButton(app, text='Mostrar Mais', command=more_stats)
btn_more_stats.pack(pady=(5,5))

btn_xp20 = ctk.CTkButton(app, text='Ganhar 20XP', command=lambda: ganharxp(20))
btn_xp20.pack(pady=(5,5))

btn_xp50 = ctk.CTkButton(app, text='Ganhar 50XP', command=lambda: ganharxp(50), fg_color='green', hover_color='darkgreen')
btn_xp50.pack(pady=(5,5))






# =========================================================
# RODAPÉ
# =========================================================
'''
footer = ctk.CTkFrame(app, height=40)
footer.pack(fill="x")

footer_label = ctk.CTkLabel(
    footer,
    text="Poder Absoluto © 2026"
)
footer_label.pack(pady=10)
'''
app.mainloop()