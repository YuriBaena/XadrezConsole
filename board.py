from posicao import Posicao
from Pecas.peoes import PeaoP, PeaoB
from Pecas.torres import TorreP, TorreB
from Pecas.cavalos import CavaloP, CavaloB
from Pecas.bispos import BispoP, BispoB
from Pecas.rainhas import RainhaP, RainhaB
from Pecas.reis import ReiP, ReiB


class Tabuleiro:
    def __init__(self):
        global linhas, colunas

        self.altura = 8
        self.comprimento = 8

        self.vez = "B"  # Começa com as peças pretas

        self.posicoes = {}

        linhas = [str(i) for i in range(8, 0, -1)]
        colunas = [chr(i) for i in range(ord('a'), ord('h') + 1)]

        # Organiza o tabuleiro
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
                # Peão Preto
                elif linha == 1:
                    self.posicoes[colunas[coluna] + linhas[linha]] = Posicao(linha, coluna, PeaoP(linha, coluna))
                # Peão Branco
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

        # Atualiza os movimentos possíveis
        self.renova_movimentos_possiveis()

    def mostra(self, movimentos=None):
        if movimentos is None:
            movimentos = []  # Define uma lista vazia se nenhum movimento for especificado

        print()  # Imprime uma linha em branco

        if len(movimentos) == 0:
            # Se não houver movimentos a serem destacados, imprime o tabuleiro normalmente
            for linha in range(self.comprimento):
                print(linhas[linha], end=" |   ")  # Imprime a linha atual seguida de um separador
                for coluna in range(self.altura):
                    posicao = colunas[coluna] + linhas[linha]  # Calcula a posição atual no tabuleiro
                    if posicao in self.posicoes:
                        print(f" {self.posicoes[posicao].img} ", end="")  # Imprime a peça na posição, se existir
                    else:
                        print(f" . ", end="")  # Caso contrário, imprime um ponto para indicar posição vazia
                print()  # Nova linha após imprimir cada linha do tabuleiro

            print("  | _ _ _ _ _ _ _ _ _ _ _ _ _ ")  # Linha separadora do tabuleiro
            print("      ", end="")

            for k in colunas:
                print(f" {k} ", end="")  # Imprime os rótulos das colunas na parte inferior do tabuleiro

            print()  # Nova linha após imprimir os rótulos das colunas
        else:
            # Se houver movimentos a serem destacados, imprime o tabuleiro com esses movimentos destacados
            for linha in range(self.comprimento):
                print(linhas[linha], end=" |   ")  # Imprime a linha atual seguida de um separador
                for coluna in range(self.altura):
                    posicao = colunas[coluna] + linhas[linha]  # Calcula a posição atual no tabuleiro
                    if posicao in self.posicoes and posicao not in movimentos:
                        print(f" {self.posicoes[posicao].img} ",
                              end="")  # Imprime a peça na posição, se não for um movimento
                    elif posicao in movimentos:
                        print(f" # ", end="")  # Imprime '#' para indicar um movimento destacado
                    else:
                        print(f" . ", end="")  # Caso contrário, imprime um ponto para indicar posição vazia
                print()  # Nova linha após imprimir cada linha do tabuleiro

            print("  | _ _ _ _ _ _ _ _ _ _ _ _ _ ")  # Linha separadora do tabuleiro
            print("      ", end="")

            for k in colunas:
                print(f" {k} ", end="")  # Imprime os rótulos das colunas na parte inferior do tabuleiro

            print()  # Nova linha após imprimir os rótulos das colunas

    def escolhe(self):
        while True:
            print()

            # Escolhe peca para mover
            posicao = input("Informe a posição da peça \nque deseja usar (letra/num): ")
            if posicao in self.posicoes:

                # Verifica se e peca valida
                if self.vez == self.posicoes[posicao].peca.cor:

                    # Cria lista de possiveis movimentos
                    movimentos = self.posicoes[posicao].coordena(self.posicoes)

                    # Se tiver um ou mais movimentos entra aqui
                    if len(movimentos) != 0:
                        self.mostra(movimentos)
                        a = 0

                        # Mostra todos os possiveis movimentos
                        for i, lugar in enumerate(movimentos):
                            print(f"[ {i + 1} ] para movimentar para {lugar}")
                            a = i
                        print(f"[ {a + 2} ] para escolher outra peça")

                        # Pergunta qual movimento o jogador quer fazer
                        qual = int(input("Qual opção deseja: "))
                        if qual != a + 2:
                            pra_onde = movimentos[qual - 1]
                            peca = self.posicoes[posicao]

                            # Movimenta peca escolhida
                            self.movimenta(peca, pra_onde)

                            # Promove o peao se for necessario
                            self.promove_peao()

                            # Renova possiveis movimentos
                            self.renova_movimentos_possiveis()

                            # Verifica se algum rei esta em cheque
                            self.procura_cheque()

                            break

                    # Se nao tiver nenhum movimento
                    else:
                        print("Não existem movimentos possíveis para essa peça")
                else:
                    print("Peça da cor errada")
            else:
                print("Posição inválida")

    def movimenta(self, peca, onde):
        coluna = onde[0]
        linha = int(onde[1])

        x = linhas.index(str(linha))
        y = colunas.index(coluna)

        x1, y1 = peca.posicao

        coluna = colunas[y1]
        linha = linhas[x1]
        coordenada = coluna + linha

        # Define qual peça vai ocupar a nova posição
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

        # Atualiza a posição da peça no tabuleiro
        self.posicoes[coordenada] = Posicao(x1, y1)
        self.posicoes[onde] = Posicao(x, y, boneco)

        # Alterna a vez do jogador
        if self.vez == "P":
            self.vez = "B"
        else:
            self.vez = "P"

    def ganhou(self):
        reis = []

        for i in self.posicoes.values():
            if i.img in "♔♚":
                reis.append(i.peca.cor)

        if "B" in reis and "P" not in reis:
            print("O vencedor foi o Branco")
        elif "P" in reis and "B" not in reis:
            print("O vencedor foi o Preto")

    def renova_movimentos_possiveis(self):
        self.movimentos_possiveis_branco = {}
        self.movimentos_possiveis_preto = {}

        for i in self.posicoes.values():
            if i.peca is not None:
                i.peca.alternativas(self.posicoes)
                if i.peca.cor == "P":
                    self.movimentos_possiveis_preto[i.peca] = i.peca.possibilidades
                else:
                    self.movimentos_possiveis_branco[i.peca] = i.peca.possibilidades

    def procura_cheque(self):

        # Verifica se o rei Branco está em xeque
        for i in self.posicoes.values():
            if i.img == "♔":
                posicao_do_rei_branco = i.posicao

        for i in self.movimentos_possiveis_preto.values():
            for posicao in i:
                if posicao == posicao_do_rei_branco:
                    print(f"\n!!!!!!!\n---O Branco está em xeque---\n!!!!!!!\n")

        # Verifica se o rei Preto está em xeque
        for i in self.posicoes.values():
            if i.img == "♚":
                posicao_do_rei_preto = i.posicao

        for i in self.movimentos_possiveis_branco.values():
            for posicao in i:
                if posicao == posicao_do_rei_preto:
                    print(f"\n!!!!!!!\n---O Preto está em xeque---\n!!!!!!!\n")

    def promove_peao(self):

        troca = ["Torre", "Cavalo", "Bispo", "Rainha"]

        for chave, valor in self.posicoes.items():

            # Promove Preto
            if valor.img == "♟" and valor.posicao[0] == 7:
                for j, i in enumerate(troca):
                    print(f"[ {j + 1} ] Deseja promover seu peao para {i}")

                while True:
                    numero = int(input("Qual opção deseja: "))

                    if numero == 1:
                        # Torre
                        self.posicoes[chave] = Posicao(self.posicoes[chave].posicao[0], self.posicoes[chave].posicao[1],
                                                       TorreP(self.posicoes[chave].posicao[0],
                                                              self.posicoes[chave].posicao[1]))
                        break
                    elif numero == 2:
                        # Cavalo
                        self.posicoes[chave] = Posicao(self.posicoes[chave].posicao[0], self.posicoes[chave].posicao[1],
                                                       CavaloP(self.posicoes[chave].posicao[0],
                                                               self.posicoes[chave].posicao[1]))
                        break
                    elif numero == 3:
                        # Bispo
                        self.posicoes[chave] = Posicao(self.posicoes[chave].posicao[0], self.posicoes[chave].posicao[1],
                                                       BispoP(self.posicoes[chave].posicao[0],
                                                              self.posicoes[chave].posicao[1]))
                        break
                    elif numero == 4:
                        # Rainha
                        self.posicoes[chave] = Posicao(self.posicoes[chave].posicao[0], self.posicoes[chave].posicao[1],
                                                       RainhaP(self.posicoes[chave].posicao[0],
                                                               self.posicoes[chave].posicao[1]))
                        break
                    else:
                        print("Opção invalida!")

            # Promove Branco
            if valor.img == "♙" and valor.posicao[0] == 0:
                for j, i in enumerate(troca):
                    print(f"[ {j} ] Deseja promover seu peao para {i}")

                while True:
                    numero = int(input("Qual opção deseja: "))

                    if numero == 1:
                        # Torre
                        self.posicoes[chave] = Posicao(self.posicoes[chave].posicao[0], self.posicoes[chave].posicao[1],
                                                       TorreB(self.posicoes[chave].posicao[0],
                                                              self.posicoes[chave].posicao[1]))
                        break
                    elif numero == 2:
                        # Cavalo
                        self.posicoes[chave] = Posicao(self.posicoes[chave].posicao[0], self.posicoes[chave].posicao[1],
                                                       CavaloB(self.posicoes[chave].posicao[0],
                                                               self.posicoes[chave].posicao[1]))
                        break
                    elif numero == 3:
                        # Bispo
                        self.posicoes[chave] = Posicao(self.posicoes[chave].posicao[0], self.posicoes[chave].posicao[1],
                                                       BispoB(self.posicoes[chave].posicao[0],
                                                              self.posicoes[chave].posicao[1]))
                        break
                    elif numero == 4:
                        # Rainha
                        self.posicoes[chave] = Posicao(self.posicoes[chave].posicao[0], self.posicoes[chave].posicao[1],
                                                       RainhaB(self.posicoes[chave].posicao[0],
                                                               self.posicoes[chave].posicao[1]))
                        break
                    else:
                        print("Opção invalida!")


tabuleiro = Tabuleiro()
while True:
    tabuleiro.mostra()
    tabuleiro.escolhe()
    if tabuleiro.ganhou():
        break
