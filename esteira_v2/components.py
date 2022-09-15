from abc import ABC, abstractmethod


class Components(ABC):

    @abstractmethod
    def create(self):
        pass


class Molde(Components):

    def __init__(self, amount) -> None:
        self.amount = amount

    def create(self):
        list_components = 2*self.amount*["Molde"]
        return list_components


class Tela(Components):

    def __init__(self, amount) -> None:
        self.amount = amount

    def create(self):
        list_components = self.amount*["Tela"]
        return list_components


class PainelControle(Components):

    def __init__(self, amount) -> None:
        self.amount = amount

    def create(self):
        list_components = self.amount*["Painel de controle"]
        return list_components


class Parafuso(Components):

    def __init__(self, amount) -> None:
        self.amount = amount

    def create(self):
        list_components = 2*self.amount*["Conjunto de parafusos"]
        return list_components


class Selo(Components):

    def __init__(self, amount) -> None:
        self.amount = amount

    def create(self):
        list_components = self.amount*["Selo"]
        return list_components
