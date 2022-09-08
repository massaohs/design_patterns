from abc import ABCMeta, abstractmethod

# interface command
class Ordem(metaclass=ABCMeta):

    @abstractmethod
    def executar(self):
        pass

### ------------------------------ passo a passo da esteira ------------------------------ ###

# comando concreto

class MoldeRetangular(Ordem):

    def __init__(self, acao) -> None:
        self.acao = acao

    def executar(self):
        self.acao.molde_retangular()

class TelaLed(Ordem):

    def __init__(self, acao) -> None:
        self.acao = acao

    def executar(self):
        self.acao.tela_led()

class PainelControle(Ordem):

    def __init__(self, acao) -> None:
        self.acao = acao

    def executar(self):
        self.acao.painel_controle()


class ParafusosInternos(Ordem):

    def __init__(self, acao) -> None:
        self.acao = acao

    def executar(self):
        self.acao.parafusos_internos()


class Secador(Ordem):

    def __init__(self, acao) -> None:
        self.acao = acao

    def executar(self):
        self.acao.secador()

    
class MoldeTrazeiro(Ordem):

    def __init__(self, acao) -> None:
        self.acao = acao

    def executar(self):
        self.acao.molde_trazeiro()


class ParafusosExternos(Ordem):

    def __init__(self, acao) -> None:
        self.acao = acao

    def executar(self):
        self.acao.parafusos_externos()

    
class Selo(Ordem):

    def __init__(self, acao) -> None:
        self.acao = acao

    def executar(self):
        self.acao.selo()


class Teste(Ordem):

    def __init__(self, acao) -> None:
        self.acao = acao

    def executar(self):
        self.acao.teste()


class Embalagem(Ordem):

    def __init__(self, acao) -> None:
        self.acao = acao

    def executar(self):
        self.acao.embalagem()


### ------------------------- exibir cada ação da linha de montagem ------------------------- ###

# receiver

class Acao:

    def molde_retangular(self):
        print('Passo 1: Molde colocado na esteira')

    def tela_led(self):
        print('Passo 2: Tela encaixada no molde')

    def painel_controle(self):
        print('Passo 3: Painel de controle adicionado')

    def parafusos_internos(self):
        print('Passo 4: Parafusos internos apertados')

    def secador(self):
        print('Passo 5: Secador acionado e volume de fios reduzidos')

    def molde_trazeiro(self):
        print('Passo 6: Molde trazeiro adicionado')

    def parafusos_externos(self):
        print('Passo 7: Parafusos externos apertados')
    
    def selo(self):
        print('Passo 8: Sedo adicionado')

    def teste(self):
        print('Passo 9: Televisor testado')

    def embalagem(self):
        print('Passo 10: Televisor embalado')


# invoker ou chamador
class Invoker:

    def __init__(self) -> None:
        self.__fila_processos = []

    def adicionar_processo_fila(self, processo):
        self.__fila_processos.append(processo)

    def execucao_processos(self):
        for procss in self.__fila_processos:
            procss.executar()


class Fabrica:
    def criar_processo(self: object, processo: str, acao: object):
        return eval(processo)(acao)  
        

class Orchestrator:

    def __init__(self: object, processos: list) -> None:
        self.processos = processos

    def run(self):
        fab = Fabrica()
        acao = Acao()
        invoker = Invoker()

        # chamador/invoker
        for processo in processos:
            parte_processo_montagem = fab.criar_processo(processo, acao)
            invoker.adicionar_processo_fila(parte_processo_montagem)

        invoker.execucao_processos()

        print('\nPROCESSO DE MONTAGEM FINALIZADO!!!')

if __name__ == '__main__':
    # cliente

    processos = ['MoldeRetangular', 'TelaLed', 'PainelControle', 'ParafusosInternos',
    'Secador', 'MoldeTrazeiro', 'ParafusosExternos', 'Selo', 'Teste', 'Embalagem']

    maestro = Orchestrator(processos)
    maestro.run()