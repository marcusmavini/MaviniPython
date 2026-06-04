from PoderAbsoluto.classes import player
import math
player1 = player.Player(
    'Lionel',
    'Humano',
    'Condutor',
    1,
    100,
    200,

    {
        'Força':15,
        'Agilidade':14,
        'Vitalidade':13,
        'Inteligência':12,
        'Vontade':11,
        'Presença':10
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
        'Reputação':50,
        'Infâmia':0,
        'Notoriedade':20
    }
)

player1.stats()
player1.gainXP(150)
player1.show_level()
player1.gainXP(15)
player1.show_level()
player1.gainXP(85)
player1.show_level()