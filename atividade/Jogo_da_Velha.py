class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = [' ' for _ in range(9)]
        self.jogador_atual = 'X'

    def print_tabuleiro(self):
        for i in range(3):
            print('|'.join(self.tabuleiro[i * 3:(i + 1) * 3]))
            if i < 2:
                print('-----')

    def movimento(self, posicao):
        if self.tabuleiro[posicao] == ' ':
            self.tabuleiro[posicao] = self.jogador_atual
            if self.jogador_atual == 'X':
                self.jogador_atual = 'O'
            else:
                self.jogador_atual = 'X'
        else:
            print("Posição já ocupada!")

    def verificar_vitoria(self):
        combinacoes = [(0, 1, 2), (3, 4, 5), (6, 7, 8), 
                       (0, 3, 6), (1, 4, 7), (2, 5, 8), 
                       (0, 4, 8), (2, 4, 6)]
        for (a, b, c) in combinacoes:
            if self.tabuleiro[a] == self.tabuleiro[b] == self.tabuleiro[c] and self.tabuleiro[a] != ' ':
                return True
        return False

    def verificar_empate(self):
        return ' ' not in self.tabuleiro

    def jogar(self):
        while True:
            self.print_tabuleiro()
            posicao = int(input(f"Jogador {self.jogador_atual}, escolha uma posição (0-8): "))
            self.movimento(posicao)
            if self.verificar_vitoria():
                self.print_tabuleiro()
                print(f"Jogador {self.jogador_atual} venceu!")
                break
            if self.verificar_empate():
                self.print_tabuleiro()
                print("Empate!")
                break

jogo = JogoDaVelha()
jogo.jogar()
