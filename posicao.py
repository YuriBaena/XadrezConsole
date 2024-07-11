class Posicao:
    def __init__(self, x, y, peca=None):

        self.posicao = [x, y]

        if peca is not None:
            self.ocupado = True
            self.img = peca.ele
            self.peca = peca
            self.peca.alternativas()
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
        if self.peca is None:
            return []

        lista = list(self.peca.possibilidades)  # Evita alterar o objeto original

        quais_remover = []
        for chave, valor in posicoes.items():
            for i in range(len(lista)):
                if lista[i] == valor.posicao:
                    if valor.peca is not None and valor.peca.cor == self.peca.cor:
                        quais_remover.append(lista[i])
        for i in quais_remover:
            lista.remove(i)

        if str(self.peca)[15:21].lower() != "cavalo":
            lista = self.remover_desconectados(lista)

        linhas = [str(i) for i in range(8, 0, -1)]
        colunas = [chr(i) for i in range(ord('a'), ord('h') + 1)]

        tudo = []

        for pos in lista:
            x, y = pos
            if 0 <= x < 8 and 0 <= y < 8:
                coord = colunas[y] + linhas[x]
                tudo.append(coord)

        return tudo

    def distancia(self, pos1, pos2):
        return ((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2) ** 0.5

    def remover_desconectados(self, lista):
        def is_adjacente(pos1, pos2):
            return abs(pos1[0] - pos2[0]) <= 1 and abs(pos1[1] - pos2[1]) <= 1

        distancias = [(pos, self.distancia(pos, (self.posicao[0], self.posicao[1]))) for pos in lista]
        distancias.sort(key=lambda item: item[1])

        conectados = set()
        conectados.add(tuple(self.posicao))  # Converte (x, y) para uma tupla

        for pos, dist in distancias:
            conectado = False
            for conectado_pos in conectados:
                if is_adjacente(pos, conectado_pos):
                    conectado = True
                    break
            if not conectado:
                lista.remove(pos)
            else:
                conectados.add(tuple(pos))  # Converte pos para uma tupla antes de adicionar ao conjunto

        return lista
