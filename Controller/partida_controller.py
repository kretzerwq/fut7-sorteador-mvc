from Model.jogador import Jogador
from Model.partida import Partida

class PartidaController:
    def __init__(self):
        self.__partida = Partida()

    def adicionar_jogador(self, nome, posicao):
        if len(self.__partida.lista_confirmados) >= 14:
            return False
        for jogador in self.__partida.lista_confirmados:
            if jogador.jogador.lower() == nome.lower():
                return False
        novo_jogador = Jogador(nome, posicao)
        self.__partida.adicionar_jogador(novo_jogador)
        return True

    def remover_jogador(self, nome):
        for jogador in self.__partida.lista_confirmados:
            if jogador.jogador.lower() == nome.lower():
                self.__partida.remover_jogador(jogador)
                return True
        return False

    def sortear_times(self):
        return self.__partida.sortear_time()

    def listar_jogadores(self):
        return self.__partida.lista_confirmados