from abstract_command import Processo

### ------------------------------ passo a passo da esteira ------------------------------ ###

# comando concreto

class MoldeRetangular(Processo):

    def __init__(self, acao) -> None:
        self.acao = acao

    def executar(self):
        self.acao.molde_retangular()

class TelaLed(Processo):

    def __init__(self, acao) -> None:
        self.acao = acao

    def executar(self):
        self.acao.tela_led()

class PainelControle(Processo):

    def __init__(self, acao) -> None:
        self.acao = acao

    def executar(self):
        self.acao.painel_controle()


class ParafusosInternos(Processo):

    def __init__(self, acao) -> None:
        self.acao = acao

    def executar(self):
        self.acao.parafusos_internos()


class Secador(Processo):

    def __init__(self, acao) -> None:
        self.acao = acao

    def executar(self):
        self.acao.secador()

    
class MoldeTrazeiro(Processo):

    def __init__(self, acao) -> None:
        self.acao = acao

    def executar(self):
        self.acao.molde_trazeiro()


class ParafusosExternos(Processo):

    def __init__(self, acao) -> None:
        self.acao = acao

    def executar(self):
        self.acao.parafusos_externos()

    
class Selo(Processo):

    def __init__(self, acao) -> None:
        self.acao = acao

    def executar(self):
        self.acao.selo()


class Teste(Processo):

    def __init__(self, acao) -> None:
        self.acao = acao

    def executar(self):
        self.acao.teste()


class Embalagem(Processo):

    def __init__(self, acao) -> None:
        self.acao = acao

    def executar(self):
        self.acao.embalagem()