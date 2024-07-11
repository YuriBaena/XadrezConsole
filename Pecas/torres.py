class TorreP:
    def __init__(self, x, y):
        self.ele = "♜"
        self.cor = "P"

        self.posicao = [x, y]

    def alternativas(self):
        # Movimentos verticais da torre
        self.possibilidades = []

        #Vertical
        for i in range(8):
            possivel = [i, self.posicao[1]]
            if possivel != self.posicao:
                self.possibilidades.append(possivel)

        #Horizontal
        for j in range(8):
            possivel = [self.posicao[0], j]
            if possivel != self.posicao:
                self.possibilidades.append(possivel)


class TorreB:
    def __init__(self, x, y):
        self.ele = "♖"
        self.cor = "B"

        self.posicao = [x, y]

    def alternativas(self):
        # Movimentos verticais da torre
        self.possibilidades = []

        # Vertical
        for i in range(8):
            possivel = [i, self.posicao[1]]
            if possivel != self.posicao:
                self.possibilidades.append(possivel)

        # Horizontal
        for j in range(8):
            possivel = [self.posicao[0], j]
            if possivel != self.posicao:
                self.possibilidades.append(possivel)

