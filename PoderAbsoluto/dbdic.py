attrPlayer = {
    'hp':1000,
    'dmg':100,
    'dmg-fire':0,
    'nrg':0
}

inventory = {
    'weapon':'',
    'accessory':'',
}

#======classes========
classeElemental = {
    'name':'Elemental',
    'desc':'Controla os elementos.',

    'hp':800,
    'dmg':75
}

classeOlimpico = {
    'name':'Olímpico',
    'desc':'O melhor dos melhores.',

    'hp':800,
    'dmg':75
}
classes = [classeElemental, classeOlimpico]
#=============ORIGEM=============
originTitanico = {
    'name':'Titãnico',
    'desc':'Alta aptidão física.',

    'hp':1000,
    'dmg':100,
    'nrg':50
}

originSintetico = {
    'name':'Sintético',
    'desc':'Você e tecnologia andam juntos',

    'hp':900,
    'dmg':85,
    'nrg':100
}
#======================================
pssv_PirocineseQueimadura = {
    'name':'Queimadura',
    'desc':f'Queima inimigos. Causa {attrPlayer['dmg-fire']*0.05} de dano de fogo por turno.',

    'dmg-fire':attrPlayer['dmg-fire']*0.05,
    'msg':'Queimando...'
}

skill_PirocineseBolaDeFogo = {
    'name':'Bola de Fogo',
    'desc':f'Lança uma bola de fogo. Causa {attrPlayer['dmg-fire']*0.12} de dano de fogo.',

    'dmg-fire':attrPlayer['dmg-fire']*0.12,
    'msg':'Lançou uma bola de fogo!'
}

chipPirocinese = {
    'name':'Pirocinese',
    'desc':'O poder do fogo em suas mãos!',
    'classe':'Elemental',

    'dmg':150,
    'dmg-fire':100,

    'pssv':pssv_PirocineseQueimadura,
    'skill':skill_PirocineseBolaDeFogo
}

slots = []

originPlayer = {
    'name':'',
    'desc':'',

    'hp':0,
    'dmg':0
}

