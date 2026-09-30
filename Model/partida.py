import random
from Model.jogador import Jogador

class Partida:
    def __init__(self):
        self.__lista_confirmados = []
        self.__time_preto = []
        self.__time_branco = []

    @property
    def lista_confirmados(self):
        return self.__lista_confirmados

    @property
    def time_preto(self):
        return self.__time_preto

    @property
    def time_branco(self):
            return self.__time_branco

    def adicionar_jogador(self, jogador):
        if isinstance(jogador, Jogador):
             self.__lista_confirmados.append(jogador)

    def remover_jogador(self, jogador):
         if isinstance(jogador, Jogador):
              self.__lista_confirmados.remove(jogador)

    def sortear_time(self):
        self.__time_branco = []
        self.__time_preto = []
        goleiros = []
        linha = []
        for jogador in self.__lista_confirmados:
            if jogador.goleiro():
                goleiros.append(jogador)
            else:
                 linha.append(jogador)

        random.shuffle(goleiros)
        random.shuffle(linha)
        self.__time_branco.append(goleiros[0])
        self.__time_preto.append(goleiros[1])
        metade = len(linha)//2
        self.__time_branco.extend(linha[metade:])
        self.__time_preto.extend(linha[:metade])

        return self.__time_preto, self.__time_branco