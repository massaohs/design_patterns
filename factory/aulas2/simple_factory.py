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

    @staticmethod
    def get_carro(tipo: str) -> Veiculo:

        dict_tipo = {
            'luxo': CarroLuxo,
            'popular': CarroPopular
        }

        return dict_tipo[tipo]()


if __name__ == "__main__":

    carros_disponiveis = ['luxo', 'popular']

    for k in range(10):
        carro = VeiculoFactory.get_carro(choice(carros_disponiveis))
        carro.buscar_cliente() 