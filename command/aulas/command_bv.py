from abc import ABCMeta, abstractmethod

# interface command
class Ordem(metaclass=ABCMeta):

    @abstractmethod
    def executar(self):
        pass

# o comando concreto é representado pelas classes OrdemCompra e OrdemVenda
# podemos ter quantos "comandos concretos" forem necessários

# comando concreto
class OrdemCompra(Ordem):

    def __init__(self, acao) -> None:
        self.acao = acao

    def executar(self):
        self.acao.comprar()

# comando concreto
class OrdemVenda(Ordem):

    def __init__(self, acao) -> None:
        self.acao = acao

    def executar(self):
        self.acao.vender()

# receiver

# apesar do diagrama apresentar apenas um método que executa alguma ação, 
# na implementação temos dois métodos com ações diferentes
class Acao:

    def comprar(self):
        print('Você irá comprar ações...')

    def vender(self):
        print('Você irá vender ações...')

# invoker ou chamador

# intermediário entre o cliente e a corretora. É este que adiciona
# as ordens em uma fila de execução e as executa.
class Agente:

    def __init__(self) -> None:
        self.__fila_ordens = []

    def adicionar_ordem_fila(self, ordem):
        self.__fila_ordens.append(ordem)
        ordem.executar()

# O cliente criar as ordens de compra e venda da ações 
# e informa ao agente que adiciona na fila de execução

if __name__ == '__main__':
    # cliente
    acao = Acao()
    ordem_compra = OrdemCompra(acao)
    ordem_venda = OrdemVenda(acao)

    # chamador/invoker

    agente = Agente()
    agente.adicionar_ordem_fila(ordem_compra)
    agente.adicionar_ordem_fila(ordem_venda)