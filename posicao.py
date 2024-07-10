class Posicao:
    def __init__(self, x, y, peca=None):

        self.posicao = [x, y]

        if peca is not None:
            self.ocupado = True
            self.img = peca.ele
            self.peca = peca
            self.peca.alternativas()
            self.possivel = self.coordena(self.peca.possibilidades)
        else:
            self.ocupado = False
            self.img = "."
            self.peca = peca

    def coordena(self, lista=[]):

        linhas = [str(i) for i in range(8, 0, -1)]
        colunas = [chr(i) for i in range(ord('a'), ord('h') + 1)]

        tudo = []

        for pos in lista:
            x, y = pos
            if 0 <= x < 8 and 0 <= y < 8:
                coord = colunas[y] + linhas[x]
                tudo.append(coord)

        return tudo