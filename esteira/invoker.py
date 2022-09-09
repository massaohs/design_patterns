# invoker ou chamador
class Invoker:

    def __init__(self) -> None:
        self.__fila_processos = []

    def adicionar_processo_fila(self, processo):
        self.__fila_processos.append(processo)

    def execucao_processos(self):
        for procss in self.__fila_processos:
            procss.executar()