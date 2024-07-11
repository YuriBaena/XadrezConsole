class Posicao:
    def __init__(self, x, y, peca=None):

        self.posicao = [x, y]

        if peca is not None:
            self.ocupado = True
            self.img = peca.ele
            self.peca = peca
        else:
            self.ocupado = False
            self.img = "."
            self.peca = peca

        pecas = ["♟♙", "♝♗", "♘♞", "♛♕", "♚♔", "♜♖"]

        if self.img in pecas[0]:
            self.nome = "Peao"
        elif self.img in pecas[1]:
            self.nome = "Bispo"
        elif self.img in pecas[2]:
            self.nome = "Cavalo"
        elif self.img in pecas[3]:
            self.nome = "Rainha"
        elif self.img in pecas[4]:
            self.nome = "Rei"
        elif self.img in pecas[5]:
            self.nome = "Torre"

    def coordena(self, posicoes):

        self.peca.alternativas(posicoes)

        if self.peca is None:
            return []

        lista = list(self.peca.possibilidades)  # Evita alterar o objeto original

        #Tira possibilidades de comer propria peca
        quais_remover = []
        for chave, valor in posicoes.items():
            for i in range(len(lista)):
                if lista[i] == valor.posicao:
                    if valor.peca is not None and valor.peca.cor == self.peca.cor:
                        quais_remover.append(lista[i])
        for i in quais_remover:
            lista.remove(i)

        linhas = [str(i) for i in range(8, 0, -1)]
        colunas = [chr(i) for i in range(ord('a'), ord('h') + 1)]

        tudo = []

        for pos in lista:
            x, y = pos
            if 0 <= x < 8 and 0 <= y < 8:
                coord = colunas[y] + linhas[x]
                tudo.append(coord)

        return tudo
