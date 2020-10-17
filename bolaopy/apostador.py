
class Apostador():
    """ Classe responsavel por registar os apostadores que podem participar do bolao """
    
    def __init__ (self, nome, login, senha, credito=10.00):
        """ Inicializa / cria uma apostador valido  """
        self.nome = nome
        self.login = login
        self.senha = senha
        self.credito = credito
        self.premiacao_ganha = 0

    def apostar_valor(self, valor=5.00):
        """ Abatate valor da aposta realizada no credito do apostador  """
        self.credito -= valor

    def adicionar_credito(self, credito):
        """ Adiciona credito na conta do apostador  """
        self.credito += credito

    def converter_premiacao_em_credito(self):
        """ Converte a premiacao dos apostadores vencedores do bolao em credito """
        pass
