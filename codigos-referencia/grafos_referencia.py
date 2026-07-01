"""
Estruturas de Dados II - Grafos
Código de referência com lista de adjacência, BFS, DFS e caminho simples.
"""

from collections import deque


class Grafo:
    def __init__(self, dirigido=False):
        self.dirigido = dirigido
        self.adjacencia = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.adjacencia:
            self.adjacencia[vertice] = []

    def adicionar_aresta(self, origem, destino):
        self.adicionar_vertice(origem)
        self.adicionar_vertice(destino)

        if destino not in self.adjacencia[origem]:
            self.adjacencia[origem].append(destino)

        if not self.dirigido:
            if origem not in self.adjacencia[destino]:
                self.adjacencia[destino].append(origem)

    def mostrar(self):
        for vertice in sorted(self.adjacencia):
            print(f"{vertice} -> {self.adjacencia[vertice]}")

    def bfs(self, inicio):
        if inicio not in self.adjacencia:
            return []

        visitados = set()
        fila = deque([inicio])
        ordem = []

        while fila:
            atual = fila.popleft()

            if atual not in visitados:
                visitados.add(atual)
                ordem.append(atual)

                for vizinho in self.adjacencia[atual]:
                    if vizinho not in visitados:
                        fila.append(vizinho)

        return ordem

    def dfs(self, inicio):
        if inicio not in self.adjacencia:
            return []

        visitados = set()
        ordem = []

        def visitar(vertice):
            visitados.add(vertice)
            ordem.append(vertice)

            for vizinho in self.adjacencia[vertice]:
                if vizinho not in visitados:
                    visitar(vizinho)

        visitar(inicio)
        return ordem

    def existe_caminho(self, origem, destino):
        return destino in self.bfs(origem)

    def menor_caminho_nao_ponderado(self, origem, destino):
        if origem not in self.adjacencia or destino not in self.adjacencia:
            return None

        visitados = set()
        fila = deque([(origem, [origem])])

        while fila:
            atual, caminho = fila.popleft()

            if atual == destino:
                return caminho

            if atual not in visitados:
                visitados.add(atual)

                for vizinho in self.adjacencia[atual]:
                    if vizinho not in visitados:
                        fila.append((vizinho, caminho + [vizinho]))

        return None


if __name__ == "__main__":
    g = Grafo()

    arestas = [
        ("A", "B"),
        ("A", "C"),
        ("B", "D"),
        ("C", "D"),
        ("D", "E"),
        ("E", "F"),
    ]

    for origem, destino in arestas:
        g.adicionar_aresta(origem, destino)

    print("Lista de adjacencia:")
    g.mostrar()

    print("\nBFS saindo de A:", g.bfs("A"))
    print("DFS saindo de A:", g.dfs("A"))
    print("Existe caminho de A ate F?", g.existe_caminho("A", "F"))
    print("Menor caminho de A ate F:", g.menor_caminho_nao_ponderado("A", "F"))

    disciplinas = Grafo(dirigido=True)
    disciplinas.adicionar_aresta("Logica", "Programacao")
    disciplinas.adicionar_aresta("Programacao", "ED I")
    disciplinas.adicionar_aresta("ED I", "ED II")

    print("\nGrafo dirigido de disciplinas:")
    disciplinas.mostrar()
