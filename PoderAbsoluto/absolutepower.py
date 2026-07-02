from classes import player, origin
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
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)

# =========================================================
# ORIGENS
# =========================================================
originHuman = origin.Origin(
    'O0H',
    'Humano',
    'Um ser humano normal',
    '',
    {
        'Presence':1,
        'Inteligence':1,
    },
    {
        'Health':57,
        'Physical Damage':27,
    },
    {
        'Notoriety':1,
    },
    'origin.pssvHumano',
    ''
)

originTitan = origin.Origin(
    'O1T',
    'Titânico',
    'Muito forte que o normal',
    '',
    {
        'Strenght':1,
        'Vitality':1,
    },
    {
        'Health':100,
        'Physical Damage':80,
    },
    {
        'Notoriety':0,
    },
    'a',
    ''
)

origins_list = [originHuman, originTitan]

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

origin1ChoiceDescription = [
    {
        'name':'Humano',
        'description':'São a base de toda a civilização. Sem asas, sem poderes inatos, sem heranças cósmicas ou mutações extraordinárias, eles dependem exclusivamente de sua capacidade de aprender, adaptar-se e superar desafios.',
        'attributes':('Adaptabilidade Humana','+1 em todos os Atributos'),
        'passive':('Especialização','Escolha uma Expertise. Você recebe vantagem em testes relacionados a ela.'),
        'code':'O0H'
    },

    {
        'name':'Titânico',
        'description':'Nasceram com corpos muito além dos limites normais da vida. Seus músculos, ossos, órgãos e estrutura física foram moldados para suportar forças que destruiriam qualquer ser comum.',
        'attributes':('Corpo Monumental','+1 em FORÇA\n+1 em VITALIDADE'),
        'passive':('Constituição Titânica','Seus Pontos de Vida máximos aumentam em 10%'),
        'code':'O1T'
    },

    {
        'name':'Mutante',
        'description':'Carregam uma alteração genética rara, capaz de despertar capacidades extraordinárias impossíveis para um ser humano comum.',
        'attributes':('Mutação','+1 em INTELIGÊNCIA\n+1 em AGILIDADE'),
        'passive':('Gene Evolutivo','Adquire pequenas características ao longo da evolução'),
        'code':'O2M'
    },

    {
        'name':'Condutor',
        'description': 'Indivíduos capazes de servir como receptáculos, canais ou âncoras para energias superiores. Seu corpo simplesmente possui a rara capacidade de receber, armazenar, amplificar e canalizar forças externas.',
        'attributes':('Canal Vivo','+1 em VONTADE\n+1 em CARISMA'),
        'passive':('Reserva Energética','Ao iniciar uma batalha, a primeira habilidade tem custo 0'),
        'code':'O1T'
    }
]

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

def chooseOrigin(code):
    print(code)
    for origin in origins_list:
        print(f'{origin.name} > {origin.code}\n')
        if code == origin.code:
            print(f'Achei! {origin.code}\n')
            for attribute in origin.attr:
                if attribute in player1.attr:
                    player1.attr[attribute] += origin.attr[attribute]
                else:
                    pass
                    #player1.attr[attribute] = origin.attr[attribute]
    
    player1.show_attr()


def create_profile():
    title_create_profile = ctk.CTkLabel(main_frame, text='Criar Perfil', font=('Verdana', 20, 'bold'))
    title_create_profile.pack(pady=5)

    enter_name = ctk.CTkEntry(main_frame, placeholder_text='Nome', width=150)
    enter_name.pack(pady=5)

    line_origin_choice = ctk.CTkFrame(main_frame, fg_color='green')
    line_origin_choice.pack(fill='x')


    for origin in origin1ChoiceDescription:
        card = ctk.CTkFrame(line_origin_choice, width=180)
        card.pack(padx=5, pady=10, side='left', expand=True)
        card.pack_propagate(False)

        oName = ctk.CTkLabel(card, text=origin['name'])
        oName.pack()

        oDesc = ctk.CTkLabel(card, text=origin['description'])
        oDesc.pack()
        oDesc.pack_propagate(True)

        oAttrTitle = ctk.CTkLabel(card, text=origin['attributes'][0])
        oAttrTitle.pack()

        oAttr = ctk.CTkLabel(card, text=origin['attributes'][1])
        oAttr.pack()

        oChoice = ctk.CTkButton(card, text=f'Escolher {origin['name']}', command=lambda:chooseOrigin(origin['code']))
        oChoice.pack(pady=10)


    



# =========================================================
# CONTAINER PRINCIPAL
# =========================================================

container = ctk.CTkFrame(app)
container.grid(row=0, column=0, sticky='nsew')
#container.pack(fill="both", expand=True)

# =========================================================
# LATERAL ESQUERDA
# =========================================================

left_sidebar = ctk.CTkFrame(container, width=300)
left_sidebar.pack(side="left", fill="y", padx=5, pady=5)
left_sidebar.pack_propagate(False)
# ===================== JOGADOR ==========================
player_name = ctk.CTkLabel(left_sidebar, text=f'{player1.name}', font=('Verdana', 20, 'bold'))
player_name.pack()

player_origin_classe = ctk.CTkLabel(left_sidebar, text=f'{player1.origin} | {player1.classe}', font=('Verdana', 15, 'bold'))
player_origin_classe.pack()

show_level = ctk.CTkLabel(master=left_sidebar, text=f'NÍVEL: {player1.level}\n[XP]{player1.xp}/{player1.xpMax}', font=('Verdana', 15, 'bold'))
show_level.pack()
# =====================ATRIBUTOS ==========================
title_screen_attr = ctk.CTkLabel(left_sidebar, text='Atributos', font=('Arial', 20, 'bold'))
title_screen_attr.pack(pady=(5,0))

screen_attr = ctk.CTkLabel(left_sidebar, text=f'''Força: {player1.attr['Strenght']}
Agilidade: {player1.attr['Agility']}
Vitalidade: {player1.attr['Vitality']}
[INT] {player1.attr['Inteligence']}
[VON] {player1.attr['Will']}
[PRE] {player1.attr['Presence']}''', font=('Arial', 15))
screen_attr.pack(pady=(0,10))
# ==================ATRIBUTOS SOCIAIS=======================
title_screen_socialattr = ctk.CTkLabel(left_sidebar, text='Atributos Sociais', font=('Arial', 20, 'bold'))
title_screen_socialattr.pack()

screen_socialattr = ctk.CTkLabel(left_sidebar, text=f'''[REP] {player1.sAttr['Reputation']}
[INF] {player1.sAttr['Infamy']}
[NOT] {player1.sAttr['Notoriety']}''', font=('Arial', 15))
screen_socialattr.pack()
# =========================================================
# MAIN
# =========================================================

main_frame = ctk.CTkFrame(container)
main_frame.pack(side="left", fill="both", expand=True, padx=5, pady=5)

create_profile()

# =========================================================
# LATERAL DIREITA
# =========================================================

right_sidebar = ctk.CTkFrame(container, width=250)
right_sidebar.pack(side="right", fill="y", padx=5, pady=5)
right_sidebar.pack_propagate(False)


# =========================================================
# A
# =========================================================

btn_more_stats = ctk.CTkButton(left_sidebar, text='Mostrar Mais', command=more_stats)
btn_more_stats.pack(pady=(5,5))

btn_xp20 = ctk.CTkButton(left_sidebar, text='Ganhar 20XP', command=lambda: ganharxp(20))
btn_xp20.pack(pady=(5,5))

btn_xp50 = ctk.CTkButton(left_sidebar, text='Ganhar 50XP', command=lambda: ganharxp(50), fg_color='green', hover_color='darkgreen')
btn_xp50.pack(pady=(5,5))

btn_xp500 = ctk.CTkButton(left_sidebar, text='Ganhar 1000XP', command=lambda: ganharxp(1000), fg_color='purple', hover_color='purple')
btn_xp500.pack(pady=(5,5))






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