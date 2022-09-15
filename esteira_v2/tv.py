from factory_components import FactoryComponents
from components import *

class TV50(FactoryComponents):

    def __init__(self, amount) -> None:
        self.amount = amount
        self.molde = None
        self.tela = None
        self.painel_controle = None
        self.parafusos = None

    def get_molde(self) -> Molde:
        return Molde(self.amount)

    def get_tela(self) -> Tela:
        return Tela(self.amount)

    def get_painel_controle(self) -> PainelControle:
        return PainelControle(self.amount)

    def get_parafusos(self) -> Parafuso:
        return Parafuso(self.amount)

    def get_selo(self) -> Selo:
        return Selo(self.amount)

class TV32(FactoryComponents):

    def __init__(self, amount) -> None:
        self.amount = amount
        self.molde = None
        self.tela = None
        self.painel_controle = None
        self.parafusos = None

    def get_molde(self) -> Molde:
        return Molde(self.amount)

    def get_tela(self) -> Tela:
        return Tela(self.amount)

    def get_painel_controle(self) -> PainelControle:
        return PainelControle(self.amount)

    def get_parafusos(self) -> Parafuso:
        return Parafuso(self.amount)

    def get_selo(self) -> Selo:
        return Selo(self.amount)