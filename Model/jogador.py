class Jogador:
    def __init__(self, jogador, posicao):
        self.__jogador = jogador
        self.__posicao = posicao

    @property
    def jogador(self):
        return self.__jogador
    @jogador.setter
    def jogador(self, jogador):
        self.__jogador = jogador
    
    @property
    def posicao(self):
        return self.__posicao
    @posicao.setter
    def posicao(self, posicao):
        self.__posicao = posicao

    def goleiro(self):
        return self.__posicao.lower() == 'goleiro'