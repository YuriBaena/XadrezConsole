class ReiP:
    def __init__(self, x, y):
        self.ele = "♚"
        self.cor = "P"

        self.posicao = [x, y]

    def alternativas(self, posicoes):
        self.possibilidades = []

        linhas = [str(i) for i in range(8, 0, -1)]
        colunas = [chr(i) for i in range(ord('a'), ord('h') + 1)]

        # Vertical
        for i in range(-1, 2):
            if 0 <= self.posicao[0] + i < 8:
                possivel = [self.posicao[0] + i, self.posicao[1]]

                coordenada = str(colunas[possivel[1]]) + str(linhas[possivel[0]])
                local = posicoes[coordenada].ocupado

                if local:
                    peca_no_local = posicoes[coordenada].peca.cor

                if not local or (local and peca_no_local != self.cor):
                    if possivel != self.posicao:
                        self.possibilidades.append(possivel)

        # Horizontal
        for j in range(-1, 2):
            if 0 <= self.posicao[1] + j < 8:
                possivel = [self.posicao[0], self.posicao[1] + j]

                coordenada = str(colunas[possivel[1]]) + str(linhas[possivel[0]])
                local = posicoes[coordenada].ocupado

                if local:
                    peca_no_local = posicoes[coordenada].peca.cor

                if not local or (local and peca_no_local != self.cor):
                    if possivel != self.posicao:
                        self.possibilidades.append(possivel)

        # Diag. Principal
        for k1 in range(-1, 2):
            if 0 <= self.posicao[0] + k1 < 8 and 0 <= self.posicao[1] + k1 < 8:
                possivel = [self.posicao[0] + k1, self.posicao[1] + k1]

                coordenada = str(colunas[possivel[1]]) + str(linhas[possivel[0]])
                local = posicoes[coordenada].ocupado

                if local:
                    peca_no_local = posicoes[coordenada].peca.cor

                if not local or (local and peca_no_local != self.cor):
                    if possivel != self.posicao:
                        self.possibilidades.append(possivel)

        # Diag. Secundaria
        for k1 in range(-1, 2):
            if 0 <= self.posicao[0] + k1 < 8 and 0 <= self.posicao[1] - k1 < 8:
                possivel = [self.posicao[0] + k1, self.posicao[1] - k1]

                coordenada = str(colunas[possivel[1]]) + str(linhas[possivel[0]])
                local = posicoes[coordenada].ocupado

                if local:
                    peca_no_local = posicoes[coordenada].peca.cor

                if not local or (local and peca_no_local != self.cor):
                    if possivel != self.posicao:
                        self.possibilidades.append(possivel)


class ReiB:
    def __init__(self, x, y):
        self.ele = "♔"
        self.cor = "B"

        self.posicao = [x, y]

    def alternativas(self, posicoes):
        self.possibilidades = []

        linhas = [str(i) for i in range(8, 0, -1)]
        colunas = [chr(i) for i in range(ord('a'), ord('h') + 1)]

        # Vertical
        for i in range(-1, 2):
            if 0 <= self.posicao[0] + i < 8:
                possivel = [self.posicao[0] + i, self.posicao[1]]

                coordenada = str(colunas[possivel[1]]) + str(linhas[possivel[0]])
                local = posicoes[coordenada].ocupado

                if local:
                    peca_no_local = posicoes[coordenada].peca.cor

                if not local or (local and peca_no_local != self.cor):
                    if possivel != self.posicao:
                        self.possibilidades.append(possivel)

        # Horizontal
        for j in range(-1, 2):
            if 0 <= self.posicao[1] + j < 8:
                possivel = [self.posicao[0], self.posicao[1] + j]

                coordenada = str(colunas[possivel[1]]) + str(linhas[possivel[0]])
                local = posicoes[coordenada].ocupado

                if local:
                    peca_no_local = posicoes[coordenada].peca.cor

                if not local or (local and peca_no_local != self.cor):
                    if possivel != self.posicao:
                        self.possibilidades.append(possivel)

        # Diag. Principal
        for k1 in range(-1, 2):
            if 0 <= self.posicao[0] + k1 < 8 and 0 <= self.posicao[1] + k1 < 8:
                possivel = [self.posicao[0] + k1, self.posicao[1] + k1]

                coordenada = str(colunas[possivel[1]]) + str(linhas[possivel[0]])
                local = posicoes[coordenada].ocupado

                if local:
                    peca_no_local = posicoes[coordenada].peca.cor

                if not local or (local and peca_no_local != self.cor):
                    if possivel != self.posicao:
                        self.possibilidades.append(possivel)

        # Diag. Secundaria
        for k1 in range(-1, 2):
            if 0 <= self.posicao[0] + k1 < 8 and 0 <= self.posicao[1] - k1 < 8:
                possivel = [self.posicao[0] + k1, self.posicao[1] - k1]

                coordenada = str(colunas[possivel[1]]) + str(linhas[possivel[0]])
                local = posicoes[coordenada].ocupado

                if local:
                    peca_no_local = posicoes[coordenada].peca.cor

                if not local or (local and peca_no_local != self.cor):
                    if possivel != self.posicao:
                        self.possibilidades.append(possivel)
