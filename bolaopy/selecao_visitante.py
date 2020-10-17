from selecao import Selecao

class SelecaoVisitante(Selecao):
    """ Classe concreta que herda de Selecao definindo uma selecao Visitante """
    
    def __init__(self, nome, qtd_titulos):
        """ Inicializa uma selecao visitante baseado nas caracteristicas da classe PAI """
        #super(nome, qtd_titulos)
        self.nome = nome
        self.qtd_titulos = qtd_titulos

""" if __name__ == "__main__":
    sv = SelecaoVisitante("Argentina", 3)
    print(sv) """