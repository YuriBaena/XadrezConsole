class RainhaP:
    def __init__(self, x, y):
        self.ele = "♛"
        self.cor = "P"

        self.posicao = [x, y]

    def alternativas(self, posicoes):
        self.possibilidades = []

        linhas = [str(i) for i in range(8, 0, -1)]
        colunas = [chr(i) for i in range(ord('a'), ord('h') + 1)]

        # Vertical
        # Cima
        if self.posicao[0] > 1:
            cima = self.posicao[0] + 1
        else:
            cima = 0

        for i in range(1, cima):
            # Peca na frente
            if 0 <= self.posicao[0] - i < 8:
                frente = str(colunas[self.posicao[1]]) + str(linhas[self.posicao[0] - i])
                peca_da_frente = posicoes[frente].ocupado

                possivel = [self.posicao[0] - i, self.posicao[1]]

                if peca_da_frente:
                    cor = posicoes[frente].peca.cor

                if not peca_da_frente and possivel != self.posicao:
                    self.possibilidades.append(possivel)
                elif peca_da_frente and possivel != self.posicao:
                    if cor != self.cor:
                        self.possibilidades.append(possivel)
                        break
                    else:
                        break
                else:
                    break

        # Baixo

        if self.posicao[0] < 7:
            baixo = 8 - self.posicao[0]
        else:
            baixo = 0

        for j in range(1, baixo):
            # Peca atras
            if 0 <= self.posicao[0] + j < 8:
                frente = str(colunas[self.posicao[1]]) + str(linhas[self.posicao[0] + j])
                peca_da_frente = posicoes[frente].ocupado

                possivel = [self.posicao[0] + j, self.posicao[1]]

                if peca_da_frente:
                    cor = posicoes[frente].peca.cor

                if not peca_da_frente and possivel != self.posicao:
                    self.possibilidades.append(possivel)
                elif peca_da_frente and possivel != self.posicao:
                    if cor != self.cor:
                        self.possibilidades.append(possivel)
                        break
                    else:
                        break
                else:
                    break

        # Horizontal
        # Direita
        if self.posicao[1] < 7:
            direita = 8 - self.posicao[1]
        else:
            direita = 0

        for i in range(1, direita):
            # Peca na direita
            if 0 <= self.posicao[1] + i < 8:
                frente = str(colunas[self.posicao[1] + i]) + str(linhas[self.posicao[0]])
                peca_da_frente = posicoes[frente].ocupado

                possivel = [self.posicao[0], self.posicao[1] + i]

                if peca_da_frente:
                    cor = posicoes[frente].peca.cor

                if not peca_da_frente and possivel != self.posicao:
                    self.possibilidades.append(possivel)
                elif peca_da_frente and possivel != self.posicao:
                    if cor != self.cor:
                        self.possibilidades.append(possivel)
                        break
                    else:
                        break
                else:
                    break

        # Esquerda

        if self.posicao[1] > 1:
            esquerda = self.posicao[1] + 1
        else:
            esquerda = 0

        for j in range(1, esquerda):
            # Peca na esquerda
            if 0 <= self.posicao[1] - j < 8:

                frente = str(colunas[self.posicao[1] - j]) + str(linhas[self.posicao[0]])
                peca_da_frente = posicoes[frente].ocupado

                possivel = [self.posicao[0], self.posicao[1] - j]

                if peca_da_frente:
                    cor = posicoes[frente].peca.cor

                if not peca_da_frente and possivel != self.posicao:
                    self.possibilidades.append(possivel)

                elif peca_da_frente and possivel != self.posicao:
                    if cor != self.cor:
                        self.possibilidades.append(possivel)
                        break
                    else:
                        break

                else:
                    break

        #Diagonais
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

                if not tem:
                    self.possibilidades.append(possivel)
                elif tem and cor != self.cor:
                    self.possibilidades.append(possivel)
                    break
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

                if not tem:
                    self.possibilidades.append(possivel)
                elif tem and cor != self.cor:
                    self.possibilidades.append(possivel)
                    break
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

                if not tem:
                    self.possibilidades.append(possivel)
                elif tem and cor != self.cor:
                    self.possibilidades.append(possivel)
                    break
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

                if not tem:
                    self.possibilidades.append(possivel)
                elif tem and cor != self.cor:
                    self.possibilidades.append(possivel)
                    break
                else:
                    break

            else:
                break


class RainhaB:
    def __init__(self, x, y):
        self.ele = "♕"
        self.cor = "B"

        self.posicao = [x, y]

    def alternativas(self, posicoes):
        self.possibilidades = []

        linhas = [str(i) for i in range(8, 0, -1)]
        colunas = [chr(i) for i in range(ord('a'), ord('h') + 1)]

        # Vertical
        # Cima
        if self.posicao[0] > 1:
            cima = self.posicao[0] + 1
        else:
            cima = 0

        for i in range(1, cima):
            # Peca na frente
            if 0 <= self.posicao[0] - i < 8:
                frente = str(colunas[self.posicao[1]]) + str(linhas[self.posicao[0] - i])
                peca_da_frente = posicoes[frente].ocupado

                possivel = [self.posicao[0] - i, self.posicao[1]]

                if peca_da_frente:
                    cor = posicoes[frente].peca.cor

                if not peca_da_frente and possivel != self.posicao:
                    self.possibilidades.append(possivel)
                elif peca_da_frente and possivel != self.posicao:
                    if cor != self.cor:
                        self.possibilidades.append(possivel)
                        break
                    else:
                        break
                else:
                    break

        # Baixo

        if self.posicao[0] < 7:
            baixo = 8 - self.posicao[0]
        else:
            baixo = 0

        for j in range(1, baixo):
            # Peca atras
            if 0 <= self.posicao[0] + j < 8:
                frente = str(colunas[self.posicao[1]]) + str(linhas[self.posicao[0] + j])
                peca_da_frente = posicoes[frente].ocupado

                possivel = [self.posicao[0] + j, self.posicao[1]]

                if peca_da_frente:
                    cor = posicoes[frente].peca.cor

                if not peca_da_frente and possivel != self.posicao:
                    self.possibilidades.append(possivel)
                elif peca_da_frente and possivel != self.posicao:
                    if cor != self.cor:
                        self.possibilidades.append(possivel)
                        break
                    else:
                        break
                else:
                    break

        # Horizontal
        # Direita
        if self.posicao[1] < 7:
            direita = 8 - self.posicao[1]
        else:
            direita = 0

        for i in range(1, direita):
            # Peca na direita
            if 0 <= self.posicao[1] + i < 8:
                frente = str(colunas[self.posicao[1] + i]) + str(linhas[self.posicao[0]])
                peca_da_frente = posicoes[frente].ocupado

                possivel = [self.posicao[0], self.posicao[1] + i]

                if peca_da_frente:
                    cor = posicoes[frente].peca.cor

                if not peca_da_frente and possivel != self.posicao:
                    self.possibilidades.append(possivel)
                elif peca_da_frente and possivel != self.posicao:
                    if cor != self.cor:
                        self.possibilidades.append(possivel)
                        break
                    else:
                        break
                else:
                    break

        # Esquerda

        if self.posicao[1] > 1:
            esquerda = self.posicao[1] + 1
        else:
            esquerda = 0

        for j in range(1, esquerda):
            # Peca na esquerda
            if 0 <= self.posicao[1] - j < 8:

                frente = str(colunas[self.posicao[1] - j]) + str(linhas[self.posicao[0]])
                peca_da_frente = posicoes[frente].ocupado

                possivel = [self.posicao[0], self.posicao[1] - j]

                if peca_da_frente:
                    cor = posicoes[frente].peca.cor

                if not peca_da_frente and possivel != self.posicao:
                    self.possibilidades.append(possivel)

                elif peca_da_frente and possivel != self.posicao:
                    if cor != self.cor:
                        self.possibilidades.append(possivel)
                        break
                    else:
                        break

                else:
                    break

        # Diagonais
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

                if not tem:
                    self.possibilidades.append(possivel)
                elif tem and cor != self.cor:
                    self.possibilidades.append(possivel)
                    break
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

                if not tem:
                    self.possibilidades.append(possivel)
                elif tem and cor != self.cor:
                    self.possibilidades.append(possivel)
                    break
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

                if not tem:
                    self.possibilidades.append(possivel)
                elif tem and cor != self.cor:
                    self.possibilidades.append(possivel)
                    break
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

                if not tem:
                    self.possibilidades.append(possivel)
                elif tem and cor != self.cor:
                    self.possibilidades.append(possivel)
                    break
                else:
                    break

            else:
                break
