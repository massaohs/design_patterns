

class Instalador:

    def __init__(self: object, fonte: str, destino: str) -> None:
        self.opcoes = []
        self.destino = destino
        self.fonte = fonte

    def preferencias(self, escolha):
        self.opcoes.append(escolha)

    def executar(self):
        for opcao in self.opcoes:
            print(list(opcao.values())[0])
            if list(opcao.values())[0]:
                print(f'Copiando os binários de {self.fonte} para {self.destino}')
            else:
                print('Operação Finalizada')


if __name__ == '__main__':
    # Iniciar o instalador
    instalador = Instalador('python 3.10.6.gzip', '/usr/bin/')

    # o usuário escolhe instalar apenas o python
    instalador.preferencias({'python': True})
    instalador.preferencias({'java': False})

    # execute
    instalador.executar()