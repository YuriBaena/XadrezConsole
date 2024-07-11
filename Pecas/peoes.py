class PeaoP:
    def __init__(self, i, j):
        self.ele = "♟"
        self.cor = "P"

        self.posicao = [i, j]

        if self.posicao[0] == 1 and self.posicao[1] in (0, 1, 2, 3, 4, 5, 6, 7):
            self.primeiro_mov = True
        else:
            self.primeiro_mov = False

    def alternativas(self, posicoes):

        linhas = [str(i) for i in range(8, 0, -1)]
        colunas = [chr(i) for i in range(ord('a'), ord('h') + 1)]

        #Diagonal direita
        if 0 <= self.posicao[0] + 1 < 8 and 0 <= self.posicao[1] + 1 < 8:
            dig_dir = str(colunas[self.posicao[1] + 1]) + str(linhas[self.posicao[0] + 1])

            peca_da_dig_direita = posicoes[dig_dir].peca

            # Trata diagonal direita baixo
            if peca_da_dig_direita is not None and peca_da_dig_direita.cor != self.cor:
                peca_da_dig_direita = True
            else:
                peca_da_dig_direita = False

        else:
            peca_da_dig_direita = False

        #Diagonal esquerda
        if 0 <= self.posicao[0] + 1 < 8 and 0 <= self.posicao[1] - 1 < 8:
            dig_esq = str(colunas[self.posicao[1] - 1]) + str(linhas[self.posicao[0] + 1])

            peca_da_dig_esquerda = posicoes[dig_esq].peca

            # Trata diagonal esquerda baixo
            if peca_da_dig_esquerda is not None and peca_da_dig_esquerda.cor != self.cor:
                peca_da_dig_esquerda = True
            else:
                peca_da_dig_esquerda = False

        else:
            peca_da_dig_esquerda = False

        #Primeiro movimento
        if self.primeiro_mov:

            # Peca um na frente
            frente1 = str(colunas[self.posicao[1]]) + str(linhas[self.posicao[0] + 1])
            peca_da_frente1 = posicoes[frente1].ocupado

            # Peca dois na frente
            frente2 = str(colunas[self.posicao[1]]) + str(linhas[self.posicao[0] + 2])
            peca_da_frente2 = posicoes[frente2].ocupado

            #Tudo True
            if peca_da_frente1 and peca_da_frente2 and peca_da_dig_direita and peca_da_dig_esquerda :
                self.possibilidades = [
                    (self.posicao[0] + 1, self.posicao[1] + 1),
                    (self.posicao[0] + 1, self.posicao[1] - 1)
                ]

            #Frente 1 False
            elif not peca_da_frente1 and peca_da_frente2 and peca_da_dig_direita and peca_da_dig_esquerda:
                self.possibilidades = [
                    (self.posicao[0] + 1, self.posicao[1]),
                    (self.posicao[0] + 1, self.posicao[1] + 1),
                    (self.posicao[0] + 1, self.posicao[1] - 1)
                ]

            #Frente 2 False
            elif peca_da_frente1 and not peca_da_frente2 and peca_da_dig_direita and peca_da_dig_esquerda:
                self.possibilidades = [
                    (self.posicao[0] + 1, self.posicao[1] + 1),
                    (self.posicao[0] + 1, self.posicao[1] - 1)
                ]

            #Diagonal direita False
            elif peca_da_frente1 and peca_da_frente2 and not peca_da_dig_direita and peca_da_dig_esquerda:
                self.possibilidades = [
                    (self.posicao[0] + 1, self.posicao[1] - 1)
                ]

            #Diagonal esquerda False
            elif peca_da_frente1 and peca_da_frente2 and peca_da_dig_direita and not peca_da_dig_esquerda:
                self.possibilidades = [
                    (self.posicao[0] + 1, self.posicao[1] + 1)
                ]

            #Frente 1 e Frente 2 False
            elif not peca_da_frente1 and not peca_da_frente2 and peca_da_dig_direita and peca_da_dig_esquerda:
                self.possibilidades = [
                    (self.posicao[0] + 1, self.posicao[1]),
                    (self.posicao[0] + 2, self.posicao[1]),
                    (self.posicao[0] + 1, self.posicao[1] + 1),
                    (self.posicao[0] + 1, self.posicao[1] - 1)
                ]

            #Frente 1 e Diagonal direita False
            elif not peca_da_frente1 and peca_da_frente2 and not peca_da_dig_direita and peca_da_dig_esquerda:
                self.possibilidades = [
                    (self.posicao[0] + 1, self.posicao[1]),
                    (self.posicao[0] + 1, self.posicao[1] - 1)
                ]

            #Frente 1 e Diagonal esquerda False
            elif not peca_da_frente1 and peca_da_frente2 and peca_da_dig_direita and not peca_da_dig_esquerda:
                self.possibilidades = [
                    (self.posicao[0] + 1, self.posicao[1]),
                    (self.posicao[0] + 1, self.posicao[1] + 1)
                ]

            #Frente 2 e Diagonal direita False
            elif peca_da_frente1 and not peca_da_frente2 and not peca_da_dig_direita and peca_da_dig_esquerda:
                self.possibilidades = [
                    (self.posicao[0] + 1, self.posicao[1] - 1)
                ]

            #Frente 2 e Diagonal esquerda False
            elif peca_da_frente1 and not peca_da_frente2 and  peca_da_dig_direita and not peca_da_dig_esquerda:
                self.possibilidades = [
                    (self.posicao[0] + 1, self.posicao[1] + 1)
                ]

            #Diagonal direirta e Diagonal esquerda False
            elif peca_da_frente1 and  peca_da_frente2 and not peca_da_dig_direita and not peca_da_dig_esquerda:
                self.possibilidades = []

            #Frente 1 e Frente 2 e Diagonal direita False
            elif not peca_da_frente1 and not peca_da_frente2 and not peca_da_dig_direita and peca_da_dig_esquerda:
                self.possibilidades = [
                    (self.posicao[0] + 1, self.posicao[1]),
                    (self.posicao[0] + 2, self.posicao[1]),
                    (self.posicao[0] + 1, self.posicao[1] - 1)
                ]

            #Frente 1 e Frente 2 e Diagonal esquerda False
            elif not peca_da_frente1 and not peca_da_frente2 and  peca_da_dig_direita and not peca_da_dig_esquerda:
                self.possibilidades = [
                    (self.posicao[0] + 1, self.posicao[1]),
                    (self.posicao[0] + 2, self.posicao[1]),
                    (self.posicao[0] + 1, self.posicao[1] + 1)
                ]

            #Frente 1 e Diagonal direita e Diagonal esquerda False
            elif not peca_da_frente1 and peca_da_frente2 and not peca_da_dig_direita and not peca_da_dig_esquerda:
                self.possibilidades = [
                    (self.posicao[0] + 1, self.posicao[1])
                ]

            #Frente 2 e Diagonal direita e Diagonal esquerda False
            elif peca_da_frente1 and not peca_da_frente2 and not peca_da_dig_direita and not peca_da_dig_esquerda:
                self.possibilidades = []

            #Tudo False
            elif not peca_da_frente1 and not peca_da_frente2 and not peca_da_dig_direita and not peca_da_dig_esquerda:
                self.possibilidades = [
                    (self.posicao[0] + 1, self.posicao[1]),
                    (self.posicao[0] + 2, self.posicao[1])
                ]

        #Nao e primeiro movimento
        else:

            # Peca um na frente
            frente1 = str(colunas[self.posicao[1]]) + str(linhas[self.posicao[0] + 1])
            peca_da_frente1 = posicoes[frente1].ocupado

            # Tudo True
            if peca_da_frente1 and peca_da_dig_direita and peca_da_dig_esquerda:
                self.possibilidades = [
                    (self.posicao[0] + 1, self.posicao[1] + 1),
                    (self.posicao[0] + 1, self.posicao[1] - 1)
                ]

            #Frente 1 False
            elif not peca_da_frente1 and peca_da_dig_direita and peca_da_dig_esquerda:
                self.possibilidades = [
                    (self.posicao[0] + 1, self.posicao[1]),
                    (self.posicao[0] + 1, self.posicao[1] + 1),
                    (self.posicao[0] + 1, self.posicao[1] - 1)
                ]

            #Diagonal direita False
            elif peca_da_frente1 and not peca_da_dig_direita and peca_da_dig_esquerda:
                self.possibilidades = [
                    (self.posicao[0] + 1, self.posicao[1] - 1)
                ]

            #Diagonal esquerda False
            elif peca_da_frente1 and peca_da_dig_direita and not peca_da_dig_esquerda:
                self.possibilidades = [
                    (self.posicao[0] + 1, self.posicao[1] + 1)
                ]

            #Frente 1 e Diagonal direita False
            elif not peca_da_frente1 and not peca_da_dig_direita and peca_da_dig_esquerda:
                self.possibilidades = [
                    (self.posicao[0] + 1, self.posicao[1]),
                    (self.posicao[0] + 1, self.posicao[1] - 1)
                ]

            #Frente 1 e Diagonal esquerda False
            elif not peca_da_frente1 and peca_da_dig_direita and not peca_da_dig_esquerda:
                self.possibilidades = [
                    (self.posicao[0] + 1, self.posicao[1]),
                    (self.posicao[0] + 1, self.posicao[1] + 1)
                ]

            #Diagonal direita e Diagonal esquerda False
            elif peca_da_frente1 and not peca_da_dig_direita and not peca_da_dig_esquerda:
                self.possibilidades = []

            #Tudo False
            elif not peca_da_frente1 and not peca_da_dig_direita and not peca_da_dig_esquerda:
                self.possibilidades = [
                    (self.posicao[0] + 1, self.posicao[1])
                ]


class PeaoB:
    def __init__(self, i, j):
        self.ele = "♙"
        self.cor = "B"

        self.posicao = [i, j]

        if self.posicao[0] == 6 and self.posicao[1] in (0,1,2,3,4,5,6,7):
            self.primeiro_mov = True
        else:
            self.primeiro_mov = False

    def alternativas(self, posicoes):

        linhas = [str(i) for i in range(8, 0, -1)]
        colunas = [chr(i) for i in range(ord('a'), ord('h') + 1)]

        # Peca um na frente
        frente1 = str(colunas[self.posicao[1]]) + str(linhas[self.posicao[0] - 1])
        peca_da_frente1 = posicoes[frente1].ocupado

        #Diagonal direita
        if 0 <= self.posicao[0] - 1 < 8 and 0 <= self.posicao[1] + 1 < 8:
            dig_dir = str(colunas[self.posicao[1] + 1]) + str(linhas[self.posicao[0] - 1])

            peca_da_dig_direita = posicoes[dig_dir].peca

            # Trata diagonal direita baixo
            if peca_da_dig_direita is not None and peca_da_dig_direita.cor != self.cor:
                peca_da_dig_direita = True
            else:
                peca_da_dig_direita = False

        else:
            peca_da_dig_direita = False

        #Diagonal esquerda
        if 0 <= self.posicao[0] - 1 < 8 and 0 <= self.posicao[1] - 1 < 8:
            dig_esq = str(colunas[self.posicao[1] - 1]) + str(linhas[self.posicao[0] - 1])

            peca_da_dig_esquerda = posicoes[dig_esq].peca

            # Trata diagonal esquerda baixo
            if peca_da_dig_esquerda is not None and peca_da_dig_esquerda.cor != self.cor:
                peca_da_dig_esquerda = True
            else:
                peca_da_dig_esquerda = False

        else:
            peca_da_dig_esquerda = False

        # Primeiro movimento
        if self.primeiro_mov:

            # Peca dois na frente
            frente2 = str(colunas[self.posicao[1]]) + str(linhas[self.posicao[0] - 2])
            peca_da_frente2 = posicoes[frente2].ocupado


            # Tudo True
            if peca_da_frente1 and peca_da_frente2 and peca_da_dig_direita and peca_da_dig_esquerda:
                self.possibilidades = [
                    (self.posicao[0] - 1, self.posicao[1] + 1),
                    (self.posicao[0] - 1, self.posicao[1] - 1)
                ]

            # Frente 1 False
            elif not peca_da_frente1 and peca_da_frente2 and peca_da_dig_direita and peca_da_dig_esquerda:
                self.possibilidades = [
                    (self.posicao[0] - 1, self.posicao[1]),
                    (self.posicao[0] - 1, self.posicao[1] + 1),
                    (self.posicao[0] - 1, self.posicao[1] - 1)
                ]

            # Frente 2 False
            elif peca_da_frente1 and not peca_da_frente2 and peca_da_dig_direita and peca_da_dig_esquerda:
                self.possibilidades = [
                    (self.posicao[0] - 1, self.posicao[1] + 1),
                    (self.posicao[0] - 1, self.posicao[1] - 1)
                ]

            # Diagonal direita False
            elif peca_da_frente1 and peca_da_frente2 and not peca_da_dig_direita and peca_da_dig_esquerda:
                self.possibilidades = [
                    (self.posicao[0] - 1, self.posicao[1] - 1)
                ]

            # Diagonal esquerda False
            elif peca_da_frente1 and peca_da_frente2 and peca_da_dig_direita and not peca_da_dig_esquerda:
                self.possibilidades = [
                    (self.posicao[0] - 1, self.posicao[1] + 1)
                ]

            # Frente 1 e Frente 2 False
            elif not peca_da_frente1 and not peca_da_frente2 and peca_da_dig_direita and peca_da_dig_esquerda:
                self.possibilidades = [
                    (self.posicao[0] - 1, self.posicao[1]),
                    (self.posicao[0] - 2, self.posicao[1]),
                    (self.posicao[0] - 1, self.posicao[1] + 1),
                    (self.posicao[0] - 1, self.posicao[1] - 1)
                ]

            # Frente 1 e Diagonal direita False
            elif not peca_da_frente1 and peca_da_frente2 and not peca_da_dig_direita and peca_da_dig_esquerda:
                self.possibilidades = [
                    (self.posicao[0] - 1, self.posicao[1]),
                    (self.posicao[0] - 1, self.posicao[1] - 1)
                ]

            # Frente 1 e Diagonal esquerda False
            elif not peca_da_frente1 and peca_da_frente2 and peca_da_dig_direita and not peca_da_dig_esquerda:
                self.possibilidades = [
                    (self.posicao[0] - 1, self.posicao[1]),
                    (self.posicao[0] - 1, self.posicao[1] + 1)
                ]

            # Frente 2 e Diagonal direita False
            elif peca_da_frente1 and not peca_da_frente2 and not peca_da_dig_direita and peca_da_dig_esquerda:
                self.possibilidades = [
                    (self.posicao[0] - 1, self.posicao[1] - 1)
                ]

            # Frente 2 e Diagonal esquerda False
            elif peca_da_frente1 and not peca_da_frente2 and peca_da_dig_direita and not peca_da_dig_esquerda:
                self.possibilidades = [
                    (self.posicao[0] - 1, self.posicao[1] + 1)
                ]

            # Diagonal direirta e Diagonal esquerda False
            elif peca_da_frente1 and peca_da_frente2 and not peca_da_dig_direita and not peca_da_dig_esquerda:
                self.possibilidades = []

            # Frente 1 e Frente 2 e Diagonal direita False
            elif not peca_da_frente1 and not peca_da_frente2 and not peca_da_dig_direita and peca_da_dig_esquerda:
                self.possibilidades = [
                    (self.posicao[0] - 1, self.posicao[1]),
                    (self.posicao[0] - 2, self.posicao[1]),
                    (self.posicao[0] - 1, self.posicao[1] - 1)
                ]

            # Frente 1 e Frente 2 e Diagonal esquerda False
            elif not peca_da_frente1 and not peca_da_frente2 and peca_da_dig_direita and not peca_da_dig_esquerda:
                self.possibilidades = [
                    (self.posicao[0] - 1, self.posicao[1]),
                    (self.posicao[0] - 2, self.posicao[1]),
                    (self.posicao[0] - 1, self.posicao[1] + 1)
                ]

            # Frente 1 e Diagonal direita e Diagonal esquerda False
            elif not peca_da_frente1 and peca_da_frente2 and not peca_da_dig_direita and not peca_da_dig_esquerda:
                self.possibilidades = [
                    (self.posicao[0] - 1, self.posicao[1])
                ]

            # Frente 2 e Diagonal direita e Diagonal esquerda False
            elif peca_da_frente1 and not peca_da_frente2 and not peca_da_dig_direita and not peca_da_dig_esquerda:
                self.possibilidades = []

            # Tudo False
            elif not peca_da_frente1 and not peca_da_frente2 and not peca_da_dig_direita and not peca_da_dig_esquerda:
                self.possibilidades = [
                    (self.posicao[0] - 1, self.posicao[1]),
                    (self.posicao[0] - 2, self.posicao[1])
                ]

        # Nao e primeiro movimento
        else:

            # Tudo True
            if peca_da_frente1 and peca_da_dig_direita and peca_da_dig_esquerda:
                self.possibilidades = [
                    (self.posicao[0] - 1, self.posicao[1] + 1),
                    (self.posicao[0] - 1, self.posicao[1] - 1)
                ]

            # Frente 1 False
            elif not peca_da_frente1 and peca_da_dig_direita and peca_da_dig_esquerda:
                self.possibilidades = [
                    (self.posicao[0] - 1, self.posicao[1]),
                    (self.posicao[0] - 1, self.posicao[1] + 1),
                    (self.posicao[0] - 1, self.posicao[1] - 1)
                ]

            # Diagonal direita False
            elif peca_da_frente1 and not peca_da_dig_direita and peca_da_dig_esquerda:
                self.possibilidades = [
                    (self.posicao[0] - 1, self.posicao[1] - 1)
                ]

            # Diagonal esquerda False
            elif peca_da_frente1 and peca_da_dig_direita and not peca_da_dig_esquerda:
                self.possibilidades = [
                    (self.posicao[0] - 1, self.posicao[1] + 1)
                ]

            # Frente 1 e Diagonal direita False
            elif not peca_da_frente1 and not peca_da_dig_direita and peca_da_dig_esquerda:
                self.possibilidades = [
                    (self.posicao[0] - 1, self.posicao[1]),
                    (self.posicao[0] - 1, self.posicao[1] - 1)
                ]

            # Frente 1 e Diagonal esquerda False
            elif not peca_da_frente1 and peca_da_dig_direita and not peca_da_dig_esquerda:
                self.possibilidades = [
                    (self.posicao[0] - 1, self.posicao[1]),
                    (self.posicao[0] - 1, self.posicao[1] + 1)
                ]

            # Diagonal direita e Diagonal esquerda False
            elif peca_da_frente1 and not peca_da_dig_direita and not peca_da_dig_esquerda:
                self.possibilidades = []

            # Tudo False
            elif not peca_da_frente1 and not peca_da_dig_direita and not peca_da_dig_esquerda:
                self.possibilidades = [
                    (self.posicao[0] - 1, self.posicao[1])
                ]

