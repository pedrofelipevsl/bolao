from selecao import Selecao

class SelecaoDesafiante(Selecao):
    """ Classe concreta que herda de Selecao definindo uma selecao Desafiante """

    def __init__(self, nome, qtd_titulos):
        """ Inicializa uma selecao desafiante baseado nas caracteristicas da classe PAI """
        #super(nome, qtd_titulos)
        self.nome = nome
        self.qtd_titulos = qtd_titulos

""" if __name__ == "__main__":
    sd = SelecaoDesafiante("Brasil", 5)
    print(sd) """