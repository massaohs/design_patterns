from orchestrator import Orchestrator

if __name__ == '__main__':
    # cliente

    processos = ['MoldeRetangular', 'TelaLed', 'PainelControle', 'ParafusosInternos',
    'Secador', 'MoldeTrazeiro', 'ParafusosExternos', 'Selo', 'Teste', 'Embalagem']

    amount_types_tvs = {
        'TV32': 1
    }

    orc = Orchestrator(processos, amount_types_tvs)
    orc.run()