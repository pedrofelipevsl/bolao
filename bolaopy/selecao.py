import abc # importe necessario para tornar a classes em abstrata, faz parte da lib do python

class Selecao(abc.ABC):
    """ Classe abstrata define os atributos macros de uma selecao """
    @abc.abstractmethod
    def __init__(self, nome, qtd_titulos=0):
        """ Inicializa uma selecao para as classes filhas, pois nao pode ser istanciada pois eh abstrata """
        self.nome = nome
        self.qtd_titulos = qtd_titulos

    def __repr__(self):
        """ Retorna a representacao textual de uma selecao, a filhas herdam este metodo """
        return "Nome: %s QtdTitulos: %s" % (self.nome, self.qtd_titulos)

""" if __name__ == "__main__":
    s = Selecao("Alemanha", 4)
    print(s) """
