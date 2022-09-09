from receiver import Acao
from invoker import Invoker
from factory import Fabrica

class Orchestrator:

    def __init__(self: object, processos: list) -> None:
        self.processos = processos

    def run(self):
        fab = Fabrica()
        acao = Acao()
        invoker = Invoker()

        # chamador/invoker
        for processo in self.processos:
            parte_processo_montagem = fab.criar_processo(processo, acao)
            invoker.adicionar_processo_fila(parte_processo_montagem)

        invoker.execucao_processos()

        print('\nPROCESSO DE MONTAGEM FINALIZADO!!!')