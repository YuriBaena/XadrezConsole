from posicao import Posicao
from Pecas.peoes import PeaoP, PeaoB
from Pecas.torres import TorreP, TorreB
from Pecas.cavalos import CavaloP, CavaloB
from Pecas.bispos import BispoP, BispoB
from Pecas.rainhas import RainhaP, RainhaB
from Pecas.reis import ReiP, ReiB


class Board:
    def __init__(self):
        global linhas, colunas

        self.altura = 8
        self.comprimento = 8

        self.vez = "B"

        self.posicoes = {}

        linhas = [str(i) for i in range(8, 0, -1)]
        colunas = [chr(i) for i in range(ord('a'), ord('h') + 1)]

        for linha in range(self.comprimento):
            for coluna in range(self.altura):
                # Torre Preta
                if linha == 0 and coluna in (0, 7):
                    self.posicoes[colunas[coluna] + linhas[linha]] = Posicao(linha, coluna, TorreP(linha, coluna))
                # Cavalo Preto
                elif linha == 0 and coluna in (1, 6):
                    self.posicoes[colunas[coluna] + linhas[linha]] = Posicao(linha, coluna, CavaloP(linha, coluna))
                # Bispo Preto
                elif linha == 0 and coluna in (2, 5):
                    self.posicoes[colunas[coluna] + linhas[linha]] = Posicao(linha, coluna, BispoP(linha, coluna))
                # Rainha Preta
                elif linha == 0 and coluna == 3:
                    self.posicoes[colunas[coluna] + linhas[linha]] = Posicao(linha, coluna, RainhaP(linha, coluna))
                # Rei Preto
                elif linha == 0 and coluna == 4:
                    self.posicoes[colunas[coluna] + linhas[linha]] = Posicao(linha, coluna, ReiP(linha, coluna))
                # Peao Preto
                elif linha == 1:
                    self.posicoes[colunas[coluna] + linhas[linha]] = Posicao(linha, coluna, PeaoP(coluna))
                # Peao Branco
                elif linha == 6:
                    self.posicoes[colunas[coluna] + linhas[linha]] = Posicao(linha, coluna, PeaoB(coluna))
                # Torre Branca
                elif linha == 7 and coluna in (0, 7):
                    self.posicoes[colunas[coluna] + linhas[linha]] = Posicao(linha, coluna, TorreB(linha, coluna))
                # Cavalo Branco
                elif linha == 7 and coluna in (1, 6):
                    self.posicoes[colunas[coluna] + linhas[linha]] = Posicao(linha, coluna, CavaloB(linha, coluna))
                # Bispo Branco
                elif linha == 7 and coluna in (2, 5):
                    self.posicoes[colunas[coluna] + linhas[linha]] = Posicao(linha, coluna, BispoB(linha, coluna))
                # Rainha Branca
                elif linha == 7 and coluna == 3:
                    self.posicoes[colunas[coluna] + linhas[linha]] = Posicao(linha, coluna, RainhaB(linha, coluna))
                # Rei Branco
                elif linha == 7 and coluna == 4:
                    self.posicoes[colunas[coluna] + linhas[linha]] = Posicao(linha, coluna, ReiB(linha, coluna))
                else:
                    self.posicoes[colunas[coluna] + linhas[linha]] = Posicao(linha, coluna)

    def mostra(self, movimentos=None):

        if movimentos is None:
            movimentos = []
        print()
        if len(movimentos) == 0:
            for linha in range(self.comprimento):
                print(linhas[linha], end=" |   ")
                for coluna in range(self.altura):
                    posicao = colunas[coluna] + linhas[linha]
                    if posicao in self.posicoes:
                        print(f" {self.posicoes[posicao].img} ", end="")
                print()

            print("  | _ _ _ _ _ _ _ _ _ _ _ _ _ ")
            print("      ", end="")

            for k in colunas:
                print(f" {k} ", end="")

            print()
        else:
            for linha in range(self.comprimento):
                print(linhas[linha], end=" |   ")
                for coluna in range(self.altura):
                    posicao = colunas[coluna] + linhas[linha]
                    if posicao in self.posicoes and posicao not in movimentos:
                        print(f" {self.posicoes[posicao].img} ", end="")
                    elif posicao in movimentos:
                        print(f" # ", end="")
                print()

            print("  | _ _ _ _ _ _ _ _ _ _ _ _ _ ")
            print("      ", end="")

            for k in colunas:
                print(f" {k} ", end="")

            print()

    def escolhe(self):
        while True:
            posicao = input("Diga a posição da peça que deseja usar: ")
            if posicao in self.posicoes:
                if self.vez == self.posicoes[posicao].peca.cor:
                    movimentos = self.posicoes[posicao].possivel
                    self.mostra(movimentos)
                    break
                else:
                    print("peca da cor errada")
            else:
                print("posição invalida")


board = Board()
board.mostra()
board.escolhe()
