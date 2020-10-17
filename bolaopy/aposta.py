
class Aposta():
    """ Classe responsavel por registar as apostas realizadas pelos apostadores """
    
    def __init__(self, apostador, partida, qtd_gols_desaf, qtd_gols_visit, valor_aposta=5.00):
        """ Inicializa uma aposta com valor padrao de R$ 5,00, se não for alterado o valor na criacao """
        self.apostador = apostador
        self.partida = partida
        self.qtd_gols_desaf = qtd_gols_desaf
        self.qtd_gols_visit = qtd_gols_visit
        self.valor_aposta = valor_aposta
        