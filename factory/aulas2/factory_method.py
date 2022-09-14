from abc import ABC, abstractmethod
from random import choice


class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None:
        pass


class CarroLuxo(Veiculo):
    
    def buscar_cliente(self) -> None:
        print('Carro de luxo está buscando o cliente...')


class CarroPopular(Veiculo):
    
    def buscar_cliente(self) -> None:
        print('Carro popular está buscando o cliente...')


class VeiculoFactory(ABC):

    def __init__(self, tipo) -> None:
        self.carro = self.get_carro(tipo)

    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        pass

    def buscar_cliente(self):
        self.carro.buscar_cliente()


class ZonaSulVeiculoFactory(VeiculoFactory):
    
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        
        dict_tipo = {
            'popular': CarroPopular
        }

        return dict_tipo[tipo]()


class ZonaNorteVeiculoFactory(VeiculoFactory):
    
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        
        dict_tipo = {
            'luxo': CarroLuxo,
            'popular': CarroPopular
        }

        return dict_tipo[tipo]()

if __name__ == "__main__":

    veiculos_disponiveis_zn = ['luxo', 'popular']
    veiculos_disponiveis_zs = ['popular']

    print('Zona Norte \n')
    for k in range(10):
        carro = ZonaNorteVeiculoFactory(choice(veiculos_disponiveis_zn))
        carro.buscar_cliente()

    print('Zona Sul \n')
    for k in range(10):
        carro = ZonaSulVeiculoFactory(choice(veiculos_disponiveis_zs))
        carro.buscar_cliente()  