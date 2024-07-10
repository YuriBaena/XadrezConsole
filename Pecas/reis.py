class ReiP:
    def __init__(self, x, y):
        self.ele = "♚"
        self.cor = "P"

        self.posicao = [x, y]

    def alternativas(self):
        self.possibilidades = []

        #Vertical
        for i in range(-1, 2):
            possivel = [self.posicao[0] + i, self.posicao[1]]
            self.possibilidades.append(possivel)

        #Horizontal
        for j in range(-1, 2):
            possivel = [self.posicao[0], self.posicao[1] + j]
            self.possibilidades.append(possivel)

        #Diag. Principal
        for k1 in range(-1, 2):
            possivel = [self.posicao[0] + k1, self.posicao[1] + k1]
            self.possibilidades.append(possivel)

        # Diag. Secundaria
        for k1 in range(-1, 2):
            possivel = [self.posicao[0] + k1, self.posicao[1] - k1]
            self.possibilidades.append(possivel)

        qtd = self.possibilidades.count(self.posicao)
        for i in range(qtd):
            self.possibilidades.remove(self.posicao)

class ReiB:
    def __init__(self, x, y):
        self.ele = "♔"
        self.cor = "B"

        self.posicao = [x, y]

    def alternativas(self):
        self.possibilidades = []

        # Vertical
        for i in range(-1, 2):
            possivel = [self.posicao[0] + i, self.posicao[1]]
            self.possibilidades.append(possivel)

        # Horizontal
        for j in range(-1, 2):
            possivel = [self.posicao[0], self.posicao[1] + j]
            self.possibilidades.append(possivel)

        # Diag. Principal
        for k1 in range(-1, 2):
            possivel = [self.posicao[0] + k1, self.posicao[1] + k1]
            self.possibilidades.append(possivel)

        # Diag. Secundaria
        for k1 in range(-1, 2):
            possivel = [self.posicao[0] + k1, self.posicao[1] - k1]
            self.possibilidades.append(possivel)

        qtd = self.possibilidades.count(self.posicao)
        for i in range(qtd):
            self.possibilidades.remove(self.posicao)

if __name__ == '__main__':
    #Testa possibilidades
    '''rei_preto = ReiP(4,4)
    rei_preto.possibilidades()
    mov1 = rei_preto.possibilidades
    print(mov1)
    rei_branco = ReiB(7,7)
    rei_branco.possibilidades()
    mov2 = rei_branco.possibilidades
    print(mov2)'''