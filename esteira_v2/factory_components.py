from abc import ABC, abstractmethod
from components import *

class FactoryComponents(ABC):

    @abstractmethod
    def get_molde(self) -> Molde:
        pass

    @abstractmethod
    def get_tela(self) -> Tela:
        pass

    @abstractmethod
    def get_painel_controle(self) -> PainelControle:
        pass

    @abstractmethod
    def get_parafusos(self) -> Parafuso:
        pass

    @abstractmethod
    def get_selo(self) -> Selo:
        pass