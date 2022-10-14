from components.tvs.abstractcomponents_tv import AbstractComponentsTV

class TVFullHD(AbstractComponentsTV):
    def __init__(self, amount, type_tv) -> None:
        self.amount = amount
        self.type_tv = type_tv
        self.components = {
            "FrontMold": self.get_front_mold(),
            "BackMold": self.get_back_mold(),
            "Screen": self.get_screen(),
            "Board": self.get_board(),
            "InternalBolts": self.get_internal_bolts(),
            "ExternalBolts": self.get_external_bolts(),
            "Label": self.get_label(),
            "Tests": self.get_tests(),
            "Package": self.get_package()
        }

    def get_front_mold(self):
        return self.amount*['front_mold']

    def get_back_mold(self):
        return self.amount*['back_mold']

    def get_screen(self):
        return self.amount*['screen']

    def get_board(self):
        return self.amount*['board']

    def get_internal_bolts(self):
        return self.amount*['internal_bolts']

    def get_external_bolts(self):
        return self.amount*['external_bolts']

    def get_label(self):
        return self.amount*['label']

    def get_tests(self):
        return list()

    def get_package(self):
        return list()