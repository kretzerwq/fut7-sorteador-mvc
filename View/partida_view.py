from Controller.partida_controller import PartidaController
from Model.jogador import Jogador

class PartidaView:
    def __init__(self):
        self.__controller = PartidaController()

    def exibir_menu(self):
        largura = 21
        print('\n'+'='*21)
        print('MENU FUT7'.center(largura))
        print('1. Cadastrar jogador')
        print('2. Remover jogador')
        print('3. Sortear times')
        print('4. Listar jogadores')
        print('0. Sair')
        print('-'*21)

    def pedir_dados_jogador(self):
        nome = input('Digite o nome do jogador:')
        posicao = input('Posição (Goleiro/Linha): ').strip()
        return nome, posicao

    def exibir_times(self, time_branco, time_preto):
        print('===TIME BRANCO===')
        for jogador in time_branco:
            print(f'- {jogador.jogador} ({jogador.posicao})')
        print('===TIME PRETO===')
        for jogador in time_preto:
            print(f'- {jogador.jogador} ({jogador.posicao})')

    def iniciar(self):
        while True:
            self.exibir_menu()
            opcao = input('Escolha uma opção: ').strip()

            match opcao:
                case '1':
                    nome, posicao = self.pedir_dados_jogador()
                    if self.__controller.adicionar_jogador(nome, posicao):
                        print(f'Jogador {nome} adicionado com sucesso!')
                    else:
                        print('Lista cheia (máx. 14) ou jogador já cadastrado!')

                case '2':
                    nome = input('Digite o nome do jogador a remover: ').strip()
                    if self.__controller.remover_jogador(nome):
                        print(f'Jogador {nome} removido com sucesso!')
                    else:
                        print('Jogador não encontrado na lista.')

                case '3':
                    jogadores = self.__controller.listar_jogadores()
                    if len(jogadores) < 2:
                        print('Adicione mais jogadores antes de realizar o sorteio!')
                    else:
                        time_branco, time_preto = self.__controller.sortear_times()
                        self.exibir_times(time_branco, time_preto)

                case '4':
                    jogadores = self.__controller.listar_jogadores()
                    print(f'\n---Confirmados ({len(jogadores)}/14)---')
                    for jogador in jogadores:
                        print(f'- {jogador.jogador} ({jogador.posicao})')

                case '0':
                    print('\nSaindo do sistema...')
                    break

                case _:
                    print('Opção inválida! Tente novamente.')