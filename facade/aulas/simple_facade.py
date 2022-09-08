# gerenciador de eventos

# façade
from this import d


class GerenciamentoEventos:

    def __init__(self) -> None:
        print('GerenciamentoEventos :: Vou organizar com todo mundo!\n\n')

    def organizar(self):
        self.salao = SalaoFestas()
        self.salao.agendar()

        self.florista = Florista()
        self.florista.arranjar_flores()

        self.comida = Restaurante()
        self.comida.preparar()

        self.musica = Banda()
        self.musica.montar_palco()

# subsistema 1
class SalaoFestas:

    def __init__(self) -> None:
        print('SalaoFestas :: Agendado o salão de festas para o casamento...')

    def _disponibilidade(self):
        print('SalaoFestas :: Este salão está disponível?')
        return True

    def agendar(self):
        if self._disponibilidade():
            print('SalaoFestas :: Agendamento do salão realizado.\n')


# subsistema 2
class Florista:

    def __init__(self) -> None:
        print('Florista :: Florista para um evento?')

    def arranjar_flores(self):
        print('Florista :: Rosas, Margaridas, Lírios serão usadas...\n')


class Restaurante:

    def __init__(self) -> None:
        print('Restaurante :: Comida para eventos...')

    def preparar(self):
        print('Restaurante :: Comida chinesa e brasileira serão servidas...\n')


# subsistema 4
class Banda:

    def __init__(self) -> None:
        print('Banda :: Arranjos musicais para o evento...')

    def montar_palco(self):
        print('Banda :: Preparando o palco para tocar jazz e rock no evento...\n')


# cliente
class Cliente:

    def __init__(self) -> None:
        print('Cliente :: Uau! Preparação para o casamento!')

    def contrata_gerente_eventos(self):
        print('Cliente :: Vou contrar uma empresa para gerenciar eventos\n')

        gerenciamento = GerenciamentoEventos()
        gerenciamento.organizar()


    def __del__(self):
        print('Cliente :: Foi muito simples organizar este evento com o Façade...\n')

if __name__ == '__main__':
    cliente = Cliente()
    cliente.contrata_gerente_eventos()