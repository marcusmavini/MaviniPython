from PoderAbsoluto.Player import player

player1 = player.Player(
    'Lionel',
    'Humano',
    'Condutor',

    1000,
    500,
    50,
    80,
    60
)

player1.stats()

player1.hp_mod('define', 89)

player1.stats()
