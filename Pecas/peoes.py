class PeaoP:
    def __init__(self, i, j):
        self.ele = "♟"
        self.cor = "P"

        self.posicao = [i, j]

        if self.posicao[0] == 1 and self.posicao[1] in (0, 1, 2, 3, 4, 5, 6, 7):
            self.primeiro_mov = True
        else:
            self.primeiro_mov = False

    def alternativas(self):
        if self.primeiro_mov:
            self.possibilidades = [
                (self.posicao[0] + 1, self.posicao[1]),
                (self.posicao[0] + 2, self.posicao[1])
            ]
        else:
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

    def alternativas(self):
        if self.primeiro_mov:
            self.possibilidades = [
                (self.posicao[0] - 1, self.posicao[1]),
                (self.posicao[0] - 2, self.posicao[1])
            ]
        else:
            self.possibilidades = [
                (self.posicao[0] - 1, self.posicao[1])
            ]



