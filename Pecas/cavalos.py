class CavaloP:
    def __init__(self, x, y):
        self.ele = "♞"
        self.cor = "P"

        self.posicao = [x, y]

    def alternativas(self, posicoes):
        self.possibilidades = []

        linhas = [str(i) for i in range(8, 0, -1)]
        colunas = [chr(i) for i in range(ord('a'), ord('h') + 1)]

        #L para cima/baixo
        cd = [self.posicao[0] + 2, self.posicao[1] + 1]
        ce = [self.posicao[0] + 2, self.posicao[1] - 1]
        bd = [self.posicao[0] - 2, self.posicao[1] + 1]
        be = [self.posicao[0] - 2, self.posicao[1] - 1]

        #L para os lados
        dc = [self.posicao[0] + 1, self.posicao[1] + 2]
        db = [self.posicao[0] - 1, self.posicao[1] + 2]
        ec = [self.posicao[0] + 1, self.posicao[1] - 2]
        eb = [self.posicao[0] - 1, self.posicao[1] - 2]

        testes = [cd, ce, bd, be, dc, db, ec, eb]

        for i in testes:
            if (0 <= i[0] <= 7) and (0 <= i[1] <= 7):
                coordenada = str(colunas[i[1]]) + str(linhas[i[0]])
                local = posicoes[coordenada].ocupado

                if local:
                    peca_no_local = posicoes[coordenada].peca.cor

                if not local or local and peca_no_local != self.cor:
                    self.possibilidades.append(i)


class CavaloB:
    def __init__(self, x, y):
        self.ele = "♘"
        self.cor = "B"

        self.posicao = [x, y]

    def alternativas(self, posicoes):
        self.possibilidades = []

        linhas = [str(i) for i in range(8, 0, -1)]
        colunas = [chr(i) for i in range(ord('a'), ord('h') + 1)]

        # L para cima/baixo
        cd = [self.posicao[0] + 2, self.posicao[1] + 1]
        ce = [self.posicao[0] + 2, self.posicao[1] - 1]
        bd = [self.posicao[0] - 2, self.posicao[1] + 1]
        be = [self.posicao[0] - 2, self.posicao[1] - 1]

        # L para os lados
        dc = [self.posicao[0] + 1, self.posicao[1] + 2]
        db = [self.posicao[0] - 1, self.posicao[1] + 2]
        ec = [self.posicao[0] + 1, self.posicao[1] - 2]
        eb = [self.posicao[0] - 1, self.posicao[1] - 2]

        testes = [cd, ce, bd, be, dc, db, ec, eb]

        for i in testes:
            if (0 <= i[0] <= 7) and (0 <= i[1] <= 7):
                coordenada = str(colunas[i[1]]) + str(linhas[i[0]])
                local = posicoes[coordenada].ocupado

                if local:
                    peca_no_local = posicoes[coordenada].peca.cor

                if not local or (local and peca_no_local != self.cor):
                    self.possibilidades.append(i)

