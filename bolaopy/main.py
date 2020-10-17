""" importes da biblioteca Python para configuracao de data e hora """
from datetime import date, datetime

""" importes das classes de negocio da aplicacao de BOLAO """
from apostador import Apostador
from selecao_desafiante import SelecaoDesafiante
from selecao_visitante import SelecaoVisitante
from partida import Partida
from aposta import Aposta
from bolao import Bolao

class Main():
    """ Classe nucleo da aplicacao """
    def __init__(self):
        
        # criando os apostadores
        apostador1 = Apostador("Emerson","eme1","123456")
        apostador2 = Apostador("Lucas Va","lukita","123456")
        apostador3 = Apostador("Pedro F","pedroco","123456")
        apostador4 = Apostador("Lucas Vi","ligero","123456")

        # criando as selecoes desafiante e visitante
        sel_des1 = SelecaoDesafiante("Brasil", 5)
        sel_vis1 = SelecaoVisitante("Argentina", 3)

        # criando a partida
        partida1 = Partida(sel_des1, sel_vis1, "Fonte Nova", datetime.strptime('18-10-2020 16:00', '%d-%m-%Y %H:%M'))

        # criando as apostas
        aposta1 = Aposta(apostador1, partida1, 2, 0)
        aposta2 = Aposta(apostador2, partida1, 3, 1)
        aposta3 = Aposta(apostador3, partida1, 2, 1)
        aposta4 = Aposta(apostador4, partida1, 1, 1)

        #apostadores = [apostador1, apostador2, apostador3, apostador4]

        # definindo o nome do bolao
        bolao1 = Bolao(" Classico das americas: Brasil X Argentina ")

        # adicionando apostas realizadas no bolao
        bolao1.adicionar_aposta(aposta1)
        bolao1.adicionar_aposta(aposta2)
        bolao1.adicionar_aposta(aposta3)
        bolao1.adicionar_aposta(aposta4)

        #exibe as apostas associadas ao bolao informdo
        print(bolao1)

        #testando a remoção de uma aposta
        """ bolao1.remover_aposta(aposta1)
        print(bolao1)
        print("Valor total em disputa = {}".format(bolao1.valor_disputado)) """

        # definindo o placar da partida
        partida1.set_gols_desafiante(5)
        partida1.set_gols_visitante(0)

        # exibe resultado  da partida
        print(partida1)

        # apurar os possiveis vencedores em funcao do placar informado
        bolao1.verificar_vencedores()

        # exibir vencedores com o valor de sua respectiva premiacao
        print(">> Vencedores: ")
        if bolao1.vencedores:
            for ven in bolao1.vencedores:
                print(ven.nome, "\tpremio -> ", bolao1.premiacao)
        else:
            print("Ninguem acertou o bolao, sem ganhadores!")
        print("\n")
        
        # exibir os apostadores e seus crediros
        print(">> Apostadore / Creditos / Premio:")
        for ap in bolao1.apostas:
            print(ap.apostador.nome, "\tcredito -> ", ap.apostador.credito, "\tpremio -> ", ap.apostador.premiacao_ganha)

        print("\n")

        # exibir a classificacao dos apostadores (em processo de construcao)
        """ for ap in sorted(apostadores, key="premiacao_ganha", reverse=True) :
            print(ap.apostador.nome, "credito -> ", ap.apostador.premiacao_ganha)
        print("\n")  """


app_run = Main()

