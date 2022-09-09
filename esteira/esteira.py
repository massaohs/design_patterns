from orchestrator import Orchestrator

if __name__ == '__main__':
    # cliente

    processos = ['MoldeRetangular', 'TelaLed', 'PainelControle', 'ParafusosInternos',
    'Secador', 'MoldeTrazeiro', 'ParafusosExternos', 'Selo', 'Teste', 'Embalagem']

    orc = Orchestrator(processos)
    orc.run()