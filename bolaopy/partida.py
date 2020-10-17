from datetime import date, datetime

class Partida():
    """ Classe que estrutura uma partida """

    def __init__(self, sel_desaf, sel_visit, estadio, data_hora=datetime.now()):
        """ Inicializa uma partida """
        self.sel_desaf = sel_desaf
        self.sel_visit = sel_visit
        self.gols_desaf = 0
        self.gols_visit = 0
        self.estadio = estadio
        self.data_hora = data_hora

    def __repr__(self):
        """ Exibe os dados detalhados do Bolao """
        partida_str = "{:=^80}".format(" <<< >>> ") + "\n" 
        placar = " %s %d x %d %s " % (  self.sel_desaf.nome,
                                        self.gols_desaf,
                                        self.gols_visit,
                                        self.sel_visit.nome,)
        partida_str += "{: ^80}".format(" Placar da partrida >>" + placar + "<< ") + "\n" 
        partida_str += "{:=^80}".format(" <<< >>> ") + "\n"         
        return partida_str
        

    def set_gols_desafiante(self,gols):
        """ Define os gols feitos pelo desafiante """
        self.gols_desaf = gols

    def set_gols_visitante(self, gols):
        """ Define os gols feitos pelo visitante """
        self.gols_visit = gols

