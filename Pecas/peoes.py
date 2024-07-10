class PeaoP:
    def __init__(self, j):
        self.ele = "♟"
        self.cor = "P"

        self.posicao = [1, j]

        self.primeiro_mov = True

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
    def __init__(self, j):
        self.ele = "♙"
        self.cor = "B"

        self.posicao = [6, j]

        self.primeiro_mov = True

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


if __name__ == '__main__':
    # Testa possibilidades
    '''peao_preto = PeaoP(5)
    peao_preto.possibilidades()
    mov1 = peao_preto.possibilidades
    print(mov1)
    peao_branco = PeaoB(5)
    peao_branco.possibilidades()
    mov2 = peao_branco.possibilidades
    print(mov2)'''
