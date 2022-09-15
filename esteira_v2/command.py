from abstract_command import Processo

### ------------------------------ passo a passo da esteira ------------------------------ ###

# comando concreto

class MoldeRetangular(Processo):

    def __init__(self, acao) -> None:
        self.acao = acao
        

    def executar(self, tv):
        self.acao.molde_retangular(tv)

class TelaLed(Processo):

    def __init__(self, acao) -> None:
        self.acao = acao

    def executar(self, tv):
        self.acao.tela_led(tv)

class PainelControle(Processo):

    def __init__(self, acao) -> None:
        self.acao = acao

    def executar(self, tv):
        self.acao.painel_controle(tv)


class ParafusosInternos(Processo):

    def __init__(self, acao) -> None:
        self.acao = acao

    def executar(self, tv):
        self.acao.parafusos_internos(tv)


class Secador(Processo):

    def __init__(self, acao) -> None:
        self.acao = acao

    def executar(self, tv):
        self.acao.secador()

    
class MoldeTrazeiro(Processo):

    def __init__(self, acao) -> None:
        self.acao = acao

    def executar(self, tv):
        self.acao.molde_trazeiro(tv)


class ParafusosExternos(Processo):

    def __init__(self, acao) -> None:
        self.acao = acao

    def executar(self, tv):
        self.acao.parafusos_externos(tv)

    
class Selo(Processo):

    def __init__(self, acao) -> None:
        self.acao = acao

    def executar(self, tv):
        self.acao.selo(tv)


class Teste(Processo):

    def __init__(self, acao) -> None:
        self.acao = acao

    def executar(self, tv):
        self.acao.teste()


class Embalagem(Processo):

    def __init__(self, acao) -> None:
        self.acao = acao

    def executar(self, tv):
        self.acao.embalagem()