import dbdic as db

player = {
    'nome': '',
    'atributes':db.attrPlayer,
}

print('======Poder Absoluto======')
namePlayer = input('Nome: ')
player['name'] = namePlayer

print('==Escolha de Origem==')
print('Escolha a sua origem:')
originChoice = input('(1) Sintético\n(2) Titânico\n>> ')


if originChoice == '1':
    player['origin'] = db.originSintetico
    print('Você escolheu a origem Sintético!')
    db.attrPlayer['hp'] += db.originSintetico['hp']
    print(f'+{db.originSintetico['hp']} de vida')
else:
    player['origin'] = db.originTitanico
    print('Você escolheu a origem Titânico!')
    db.attrPlayer['hp'] += db.originTitanico['hp']
    print(f'+{db.originTitanico['hp']} de vida')
