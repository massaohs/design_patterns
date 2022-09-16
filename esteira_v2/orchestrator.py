from receiver import Acao
from invoker import Invoker
from factory import Fabrica
from create_components import CreateComponents
from tv import *


class Orchestrator:

    def __init__(self: object, processos: list, types_tv: dict) -> None:
        self.processos = processos
        self.types_tv = types_tv

    def run(self):
        fab = Fabrica()
        acao = Acao()
        invoker = Invoker()

        list_tvs = []

        for type_tv in self.types_tv:
            list_tvs.append(eval(type_tv)(self.types_tv[type_tv]))

        components = CreateComponents(list_tvs)
        components.create()

        # chamador/invoker
        for processo in self.processos:
            parte_processo_montagem = fab.criar_processo(processo, acao)
            invoker.adicionar_processo_fila(parte_processo_montagem)

        for tv in list_tvs:

            print(f'\nFabricando {self.types_tv[type(tv).__name__]} TVs de {type(tv).__name__}\n\n')
            
            for k in range(self.types_tv[type(tv).__name__]):
                invoker.execucao_processos(tv)

        print('\nPROCESSO DE MONTAGEM FINALIZADO!!!')