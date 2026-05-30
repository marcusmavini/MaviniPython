from PoderAbsoluto.Origins import origin
from PoderAbsoluto.Player import player

originTianico = origin.Origin(
    'Titânico',
    'O mais forte!',
    500,
    150,
    100,
)

originSintetico = origin.Origin(
    'Sintético',
    'Ama Tecnologia',
    400,
    120,
    200,
)

player1 = player.Player(
    'Marcus Mavini',
    50,
    [200, 300, 50],
    'Mochila'
)

player1.stats()

originTianico.stats()
originSintetico.stats()

