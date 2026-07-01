"""
Estruturas de Dados II - Grafos
Arquivo base para os alunos completarem durante a aula.
"""

from collections import deque


class Grafo:
    def __init__(self, dirigido=False):
        self.dirigido = dirigido
        self.adjacencia = {}

    def adicionar_vertice(self, vertice):
        # TODO: se o vertice ainda nao existir, criar uma lista vazia para ele
        pass

    def adicionar_aresta(self, origem, destino):
        # TODO:
        # 1. garantir que origem exista
        # 2. garantir que destino exista
        # 3. adicionar destino na lista de origem
        # 4. se o grafo nao for dirigido, adicionar origem na lista de destino
        pass

    def mostrar(self):
        # TODO: imprimir cada vertice e sua lista de vizinhos
        pass

    def bfs(self, inicio):
        # TODO: implementar busca em largura usando fila
        pass

    def dfs(self, inicio):
        # TODO: implementar busca em profundidade usando recursao ou pilha
        pass

    def existe_caminho(self, origem, destino):
        # TODO: usar BFS ou DFS para verificar se existe caminho
        pass


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

    g.mostrar()

    print("BFS saindo de A:", g.bfs("A"))
    print("DFS saindo de A:", g.dfs("A"))
    print("Existe caminho de A ate F?", g.existe_caminho("A", "F"))
