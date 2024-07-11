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
                    self.posicoes[colunas[coluna] + linhas[linha]] = Posicao(linha, coluna, PeaoP(linha, coluna))
                # Peao Branco
                elif linha == 6:
                    self.posicoes[colunas[coluna] + linhas[linha]] = Posicao(linha, coluna, PeaoB(linha, coluna))
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
                    else:
                        print(f" . ", end="")
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
                    else:
                        print(f" . ", end="")
                print()

            print("  | _ _ _ _ _ _ _ _ _ _ _ _ _ ")
            print("      ", end="")

            for k in colunas:
                print(f" {k} ", end="")

            print()

    def escolhe(self):
        while True:
            print()
            posicao = input("Diga a posição da peça \nque deseja usar (letra/num): ")
            if posicao in self.posicoes:
                if self.vez == self.posicoes[posicao].peca.cor:
                    movimentos = self.posicoes[posicao].coordena(self.posicoes)
                    if len(movimentos) != 0:
                        self.mostra(movimentos)
                        a = 0
                        for i, lugar in enumerate(movimentos):
                            print(f"[ {i+1} ] para movimentar para {lugar}")
                            a = i
                        print(f"[ {a + 2} ] para escolher outra peca")
                        qual = int(input("Qual opcao deseja: "))
                        if qual != a + 2:
                            pra_onde = movimentos[qual-1]
                            peca = self.posicoes[posicao]
                            self.movimenta(peca, pra_onde)
                            break
                    else:
                        print("Nao existem movimentos possiveis para essa peca")
                else:
                    print("peca da cor errada")
            else:
                print("posição invalida")

    def movimenta(self, peca, onde):

        coluna = onde[0]
        linha = int(onde[1])

        x = linhas.index(str(linha))
        y = colunas.index(coluna)

        x1, y1 = peca.posicao

        coluna = colunas[y1]
        linha = linhas[x1]
        coordenada = coluna + linha

        if peca.nome == "Peao":
            if self.vez == "P":
                boneco = PeaoP(x, y)
            else:
                boneco = PeaoB(x, y)
        elif peca.nome == "Bispo":
            if self.vez == "P":
                boneco = BispoP(x, y)
            else:
                boneco = BispoB(x, y)
        elif peca.nome == "Cavalo":
            if self.vez == "P":
                boneco = CavaloP(x, y)
            else:
                boneco = CavaloB(x, y)
        elif peca.nome == "Rainha":
            if self.vez == "P":
                boneco = RainhaP(x, y)
            else:
                boneco = RainhaB(x, y)
        elif peca.nome == "Rei":
            if self.vez == "P":
                boneco = ReiP(x, y)
            else:
                boneco = ReiB(x, y)
        elif peca.nome == "Torre":
            if self.vez == "P":
                boneco = TorreP(x, y)
            else:
                boneco = TorreB(x, y)

        self.posicoes[coordenada] = Posicao(x1, y1)
        self.posicoes[onde] = Posicao(x, y, boneco)

        if self.vez == "P":
            self.vez = "B"
        else:
            self.vez = "P"

    def ganhou(self):
        reis = []

        for i in self.posicoes.values():
            if i.img in "♔♚":
                reis.append(i.peca.cor)

        if "P" not in reis or "B" not in reis:
            return reis
        else:
            return False


board = Board()
while True:
    board.mostra()
    board.escolhe()
    if board.ganhou():
        rei = board.ganhou()
        if "B" in rei:
            print("O vencedor foi o Branco")
        else:
            print("O vencedor foi o Preto")

        break


