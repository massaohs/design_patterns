from command import *

class Fabrica:
    def criar_processo(self: object, processo: str, acao: object):
        return eval(processo)(acao)  