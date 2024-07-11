class BispoP:
    def __init__(self, x, y):
        self.ele = "♝"
        self.cor = "P"

        self.posicao = [x, y]

    def alternativas(self):

        self.possibilidades = []

        # Diagonal Principal (x + y constantes)
        for k in range(-7, 8):
            possivel1 = [self.posicao[0] + k, self.posicao[1] + k]
            if 0 <= possivel1[0] < 8 and 0 <= possivel1[1] < 8 and possivel1 != self.posicao:
                self.possibilidades.append(possivel1)

        # Diagonal Secundária (x - y constantes)
        for k in range(-7, 8):
            possivel2 = [self.posicao[0] + k, self.posicao[1] - k]
            if 0 <= possivel2[0] < 8 and 0 <= possivel2[1] < 8 and possivel2 != self.posicao:
                self.possibilidades.append(possivel2)

        # Remover posição atual das possibilidades
        self.possibilidades = [pos for pos in self.possibilidades if pos != self.posicao]


class BispoB:
    def __init__(self, x, y):
        self.ele = "♗"
        self.cor = "B"

        self.posicao = [x, y]

    def alternativas(self):
        self.possibilidades = []

        # Diagonal Principal (x + y constantes)
        for k in range(-7, 8):
            possivel1 = [self.posicao[0] + k, self.posicao[1] + k]
            if 0 <= possivel1[0] < 8 and 0 <= possivel1[1] < 8 and possivel1 != self.posicao:
                self.possibilidades.append(possivel1)

        # Diagonal Secundária (x - y constantes)
        for k in range(-7, 8):
            possivel2 = [self.posicao[0] + k, self.posicao[1] - k]
            if 0 <= possivel2[0] < 8 and 0 <= possivel2[1] < 8 and possivel2 != self.posicao:
                self.possibilidades.append(possivel2)

        # Remover posição atual das possibilidades
        self.possibilidades = [pos for pos in self.possibilidades if pos != self.posicao]


