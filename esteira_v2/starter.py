from orchestrator import Orchestrator

if __name__ == '__main__':
    # cliente

    processos = ['MoldeRetangular', 'TelaLed', 'PainelControle', 'ParafusosInternos',
    'Secador', 'MoldeTrazeiro', 'ParafusosExternos', 'Selo', 'Teste', 'Embalagem']

    qtd_tipos = {
        'TV32': 2,
        'TV50': 1
    }

    orc = Orchestrator(processos, qtd_tipos)
    orc.run()