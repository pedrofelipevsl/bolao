from aposta import Aposta

class Bolao():
    """ Classe que agregas as apostas realizadas em um bolao, verifica se houve vencedor e qual a premiacao """
    
    def __init__(self, nome):
        """ Inicializa uma instancia do bolao, com duas listas vazias de aposta e vencedores """
        self.nome = nome
        self.apostas = list([])
        self.vencedores = list([])
        self.premiacao = 0
        self.valor_disputado = 0 # novo valor gerado em cima de cada nova aposta incuida no bolao
    
    def __repr__(self):
        """ Exibe os dados detalhados do Bolao """
        bolao_str = "\n{:*^80}".format(self.nome) + "\n\n"
        bolao_str += "{:=^80}".format(" Apostas Realizadas para " + self.apostas[0].partida.sel_desaf.nome 
                                                                  + " X "  + self.apostas[0].partida.sel_visit.nome
                                                                  + " - "  + self.apostas[0].partida.data_hora.strftime('%d/%m/%Y')
                                                                  + " as " + self.apostas[0].partida.data_hora.strftime('%H:%M') + " ") + "\n" 
        for i, ap in enumerate(self.apostas): # precorre as apostas para formar uma tabela com os detalhes
            bolao_str += "{%dª aposta} -> %s    \t %s %d x %d %s \t R$ %.2f" % (i+1, ap.apostador.nome, 
                                                                                ap.partida.sel_desaf.nome,
                                                                                ap.qtd_gols_desaf,
                                                                                ap.qtd_gols_visit,
                                                                                ap.partida.sel_visit.nome,
                                                                                ap.valor_aposta) + "\n"
        bolao_str += "{:=^80}".format(" Valor total em disputa --> R$ " + str(self.valor_disputado) + " ") + "\n"         
        return bolao_str

    def adicionar_aposta(self, aposta):
        """ Adiciona aposta ao bolao """
        if aposta.apostador.credito >= aposta.valor_aposta: # so permite que a aposta seja efetivada caso o credito do apostador seja maior ou igual ao valor da aposta
            self.apostas.append(aposta)
            self.valor_disputado += aposta.valor_aposta
            aposta.apostador.apostar_valor(aposta.valor_aposta) # reduz o valor do credito do apostador
        else:
            raise ValueError("Valor do credito >>" + aposta.apostador.credito + " << atual do jogador e inferior ao valor da aposta!")

    def remover_aposta(self, aposta):
        """ Remove uma aposta do bolao """
        self.apostas.remove(aposta)
        self.valor_disputado -= aposta.valor_aposta
        aposta.apostador.adicionar_credito(aposta.valor_aposta) # devolve o valor da  aposta no credito do apostador
        
    def verificar_vencedores(self):
        """ Processa e define os vencedores ou nao do bolao  """
        for ap in self.apostas: # verifica quem acertou o bolao pelo resultado identico do placar 
            if ap.partida.gols_desaf == ap.qtd_gols_desaf and ap.partida.gols_visit == ap.qtd_gols_visit:
                self.vencedores.append(ap.apostador)
        
        if not self.vencedores: # se ninguem tiver acetado o placar verifica quem ACERTOU A VITORIA DO DESAFIANTE
            for ap in self.apostas:
                if ap.partida.gols_desaf > ap.partida.gols_visit and ap.qtd_gols_desaf > ap.qtd_gols_visit:
                    self.vencedores.append(ap.apostador)

        if not self.vencedores: # se ninguem tiver acetado o placar verifica quem ACERTOU A VITORIA DO VISITANTE
            for ap in self.apostas:
                if ap.partida.gols_desaf < ap.partida.gols_visit and ap.qtd_gols_desaf < ap.qtd_gols_visit:
                    self.vencedores.append(ap.apostador)

        if not self.vencedores: # se ninguem tiver acetado o placar verifica quem ACERTOU O EMPATE ENTRE AS SELECOES
            for ap in self.apostas:
                if ap.partida.gols_desaf == ap.partida.gols_visit and ap.qtd_gols_desaf == ap.qtd_gols_visit:
                    self.vencedores.append(ap.apostador)

        self.set_premiacao() # ao final calcula a premiacao

    def set_premiacao(self):
        """ Processa e define a premiacao ou nao do bolao, coso nao haja vencedor devolve o credito ao apstador """
        if self.vencedores: # se a lista nao estiver vazia divede o valor disputado pela quantidade de vencedores seta a premiacao
            self.premiacao = (self.valor_disputado/len(self.vencedores))
            for ven in self.vencedores: # distribui a premiacao para os vencedores
                ven.premiacao_ganha += self.premiacao  
        else: # se nao houver vencedores devolve o credito para o apostador
            for ap in self.apostas: 
                ap.apostador.adicionar_credito(ap.valor_aposta)
    