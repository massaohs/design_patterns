# receiver
### ------------------------- exibir cada ação da linha de montagem ------------------------- ###
class Acao:

    def molde_retangular(self, tv):
        print(tv.molde)
        tv.molde.pop()
        print('Passo 1: Molde colocado na esteira\n')

    def tela_led(self, tv):
        print(tv.tela)
        tv.tela.pop()
        print('Passo 2: Tela encaixada no molde\n')

    def painel_controle(self, tv):
        print(tv.painel_controle)
        tv.painel_controle.pop()
        print('Passo 3: Painel de controle adicionado\n')

    def parafusos_internos(self, tv):
        print(tv.parafusos)
        tv.parafusos.pop()
        print('Passo 4: Parafusos internos apertados\n')

    def secador(self):
        print('Passo 5: Secador acionado e volume de fios reduzidos\n')

    def molde_trazeiro(self, tv):
        print(tv.molde)
        tv.molde.pop()
        print('Passo 6: Molde trazeiro adicionado\n')

    def parafusos_externos(self, tv):
        print(tv.parafusos)
        tv.parafusos.pop()
        print('Passo 7: Parafusos externos apertados\n')
    
    def selo(self, tv):
        print(tv.selo)
        tv.selo.pop()
        print('Passo 8: Sedo adicionado\n')

    def teste(self):
        print('Passo 9: Televisor testado\n')

    def embalagem(self):
        print('Passo 10: Televisor embalado\n')