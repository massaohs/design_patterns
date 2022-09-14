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


class VeiculoFactory:

    def __init__(self, tipo) -> None:
        self.carro = self.get_carro(tipo)

    @staticmethod
    def get_carro(tipo: str) -> Veiculo:

        dict_tipo = {
            'luxo': CarroLuxo,
            'popular': CarroPopular
        }

        return dict_tipo[tipo]()

    def buscar_cliente(self):
        self.carro.buscar_cliente()


if __name__ == "__main__":

    carros_disponiveis = ['luxo', 'popular']

    for k in range(10):
        carro = VeiculoFactory(choice(carros_disponiveis))
        carro.buscar_cliente() 