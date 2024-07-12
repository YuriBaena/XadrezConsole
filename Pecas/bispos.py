class BispoP:
    def __init__(self, x, y):
        self.ele = "♝"
        self.cor = "P"

        self.posicao = [x, y]

    def alternativas(self, posicoes):

        self.possibilidades = []

        linhas = [str(i) for i in range(8, 0, -1)]
        colunas = [chr(i) for i in range(ord('a'), ord('h') + 1)]

        # Direita Cima
        if self.posicao[1] != 7:
            direita_cima = 8 - self.posicao[1] + 1
        else:
            direita_cima = 0

        for k in range(1, direita_cima):

            if 0 <= self.posicao[1] + k < 8 and 0 <= self.posicao[0] - k < 8:

                prox = colunas[self.posicao[1] + k] + linhas[self.posicao[0] - k]
                tem = posicoes[prox].ocupado

                if tem:
                    cor = posicoes[prox].peca.cor

                possivel = [self.posicao[0] - k, self.posicao[1] + k]

                if not tem or cor != self.cor:
                    self.possibilidades.append(possivel)
                else:
                    break

            else:
                break

        # Esquerda Cima
        if self.posicao[1] != 0:
            esquerda_cima = self.posicao[1] + 1
        else:
            esquerda_cima = 0

        for k in range(1, esquerda_cima):

            if 0 <= self.posicao[1] - k < 8 and 0 <= self.posicao[0] - k < 8:

                prox = colunas[self.posicao[1] - k] + linhas[self.posicao[0] - k]
                tem = posicoes[prox].ocupado

                if tem:
                    cor = posicoes[prox].peca.cor

                possivel = [self.posicao[0] - k, self.posicao[1] - k]

                if not tem or cor != self.cor:
                    self.possibilidades.append(possivel)
                else:
                    break

            else:
                break

        # Direita Baixo
        if self.posicao[1] != 7:
            direita_baixo = 8 - self.posicao[1] + 1
        else:
            direita_baixo = 0

        for k in range(1, direita_baixo):

            if 0 <= self.posicao[1] + k < 8 and 0 <= self.posicao[0] + k < 8:

                prox = colunas[self.posicao[1] + k] + linhas[self.posicao[0] + k]
                tem = posicoes[prox].ocupado

                if tem:
                    cor = posicoes[prox].peca.cor

                possivel = [self.posicao[0] + k, self.posicao[1] + k]

                if not tem or cor != self.cor:
                    self.possibilidades.append(possivel)
                else:
                    break

            else:
                break

        # Esquerda Baixo
        if self.posicao[1] != 0:
            esquerda_baixo = self.posicao[1] + 1
        else:
            esquerda_baixo = 0

        for k in range(1, esquerda_baixo):

            if 0 <= self.posicao[1] - k < 8 and 0 <= self.posicao[0] + k < 8:

                prox = colunas[self.posicao[1] - k] + linhas[self.posicao[0] + k]
                tem = posicoes[prox].ocupado

                if tem:
                    cor = posicoes[prox].peca.cor

                possivel = [self.posicao[0] + k, self.posicao[1] - k]

                if not tem or cor != self.cor:
                    self.possibilidades.append(possivel)
                else:
                    break

            else:
                break


class BispoB:
    def __init__(self, x, y):
        self.ele = "♗"
        self.cor = "B"

        self.posicao = [x, y]

    def alternativas(self, posicoes):

        self.possibilidades = []

        linhas = [str(i) for i in range(8, 0, -1)]
        colunas = [chr(i) for i in range(ord('a'), ord('h') + 1)]

        # Direita Cima
        if self.posicao[1] != 7:
            direita_cima = 8 - self.posicao[1] + 1
        else:
            direita_cima = 0

        for k in range(1, direita_cima):

            if 0 <= self.posicao[1] + k < 8 and 0 <= self.posicao[0] - k < 8:

                prox = colunas[self.posicao[1] + k] + linhas[self.posicao[0] - k]
                tem = posicoes[prox].ocupado

                if tem:
                    cor = posicoes[prox].peca.cor

                possivel = [self.posicao[0] - k, self.posicao[1] + k]

                if not tem or cor != self.cor:
                    self.possibilidades.append(possivel)
                else:
                    break

            else:
                break

        # Esquerda Cima
        if self.posicao[1] != 0:
            esquerda_cima = self.posicao[1] + 1
        else:
            esquerda_cima = 0

        for k in range(1, esquerda_cima):

            if 0 <= self.posicao[1] - k < 8 and 0 <= self.posicao[0] - k < 8:

                prox = colunas[self.posicao[1] - k] + linhas[self.posicao[0] - k]
                tem = posicoes[prox].ocupado

                if tem:
                    cor = posicoes[prox].peca.cor

                possivel = [self.posicao[0] - k, self.posicao[1] - k]

                if not tem or cor != self.cor:
                    self.possibilidades.append(possivel)
                else:
                    break

            else:
                break


        # Direita Baixo
        if self.posicao[1] != 7:
            direita_baixo = 8 - self.posicao[1] + 1
        else:
            direita_baixo = 0

        for k in range(1, direita_baixo):

            if 0 <= self.posicao[1] + k < 8 and 0 <= self.posicao[0] + k < 8:

                prox = colunas[self.posicao[1] + k] + linhas[self.posicao[0] + k]
                tem = posicoes[prox].ocupado

                if tem:
                    cor = posicoes[prox].peca.cor

                possivel = [self.posicao[0] + k, self.posicao[1] + k]

                if not tem or cor != self.cor:
                    self.possibilidades.append(possivel)
                else:
                    break

            else:
                break


        # Esquerda Baixo
        if self.posicao[1] != 0:
            esquerda_baixo = self.posicao[1] + 1
        else:
            esquerda_baixo = 0

        for k in range(1, esquerda_baixo):

            if 0 <= self.posicao[1] - k < 8 and 0 <= self.posicao[0] + k < 8:

                prox = colunas[self.posicao[1] - k] + linhas[self.posicao[0] + k]
                tem = posicoes[prox].ocupado

                if tem:
                    cor = posicoes[prox].peca.cor

                possivel = [self.posicao[0] + k, self.posicao[1] - k]

                if not tem or cor != self.cor:
                    self.possibilidades.append(possivel)
                else:
                    break

            else:
                break
