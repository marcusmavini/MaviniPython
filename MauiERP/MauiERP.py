class Maquina:
    def __init__(self, nome, opSaia, opTop, opBlusa):
        self.nome = nome
        self.opSaia = opSaia
        self.opTop = opTop
        self.opBlusa = opBlusa
    
overloque = Maquina(
    'Overloque',
    {
        'lateral':1.07,
        'elastico':0
    },
    {
        'lateral':0,
        'rodar em cima':0,
        'rodar total':0,
        'elastico':0
    },
    {
        'preparar':0
    }
)

reta = Maquina(
    'Reta',
    {
        'etiqueta':1.07,
        'fita':0
    },
    {
        'etiqueta':0,
        'fita':0,
        'fechar buraco':0,
        'elastico':0
    },
    {
        'etiqueta':0,
        'casinha botao':0,
        'limpeza':0
    }
)

colareti = Maquina(
    'Colareti',
    {
        'rebater':1.07,
        'bainha':0
    },
    0,
    {
        'bainha':0
    }
)

maquinas = {
    'over':overloque,
    'reta':reta,
    'col':colareti
}

def cadProdHora():
    producao = 0
    for hora in range(8,18):
        producao += eval(input(f'{hora}:00 >> '))
    
    return producao

def eficienciaCostura():
    print('===== Eficiência Costureira =====')
    costureira = input('Nome: ')
    
    print('[1] Overloque\n[2] Reta\n[3] Colareti')
    maquina = input('Máquina: ')