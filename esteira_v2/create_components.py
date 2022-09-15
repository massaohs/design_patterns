from tv import TV32, TV50

class CreateComponents:

    def __init__(self, type_tv) -> None:
        self.type_tv = type_tv

    def create(self):

        for tv in self.type_tv:
            molde = tv.get_molde()
            tv.molde = molde.create()

            tela = tv.get_tela()
            tv.tela = tela.create()

            painel_controle = tv.get_painel_controle()
            tv.painel_controle = painel_controle.create()

            parafusos = tv.get_parafusos()
            tv.parafusos = parafusos.create()

            selo = tv.get_selo()
            tv.selo = selo.create()

        # print(tv32.molde)
        # tv32.molde.pop()
