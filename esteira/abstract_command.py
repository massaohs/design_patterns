from abc import ABCMeta, abstractmethod

# interface command
class Processo(metaclass=ABCMeta):

    @abstractmethod
    def executar(self):
        pass