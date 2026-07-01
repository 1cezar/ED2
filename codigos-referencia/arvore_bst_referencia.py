from collections import deque


class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


class ArvoreBinaria:
    """Árvore binária comum: não possui regra de ordenação."""

    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        novo = No(valor)

        if self.raiz is None:
            self.raiz = novo
            return

        fila = deque([self.raiz])

        while fila:
            atual = fila.popleft()

            if atual.esquerda is None:
                atual.esquerda = novo
                return
            fila.append(atual.esquerda)

            if atual.direita is None:
                atual.direita = novo
                return
            fila.append(atual.direita)

    def pre_ordem(self):
        resultado = []

        def percorrer(no):
            if no:
                resultado.append(no.valor)
                percorrer(no.esquerda)
                percorrer(no.direita)

        percorrer(self.raiz)
        return resultado

    def em_ordem(self):
        resultado = []

        def percorrer(no):
            if no:
                percorrer(no.esquerda)
                resultado.append(no.valor)
                percorrer(no.direita)

        percorrer(self.raiz)
        return resultado

    def pos_ordem(self):
        resultado = []

        def percorrer(no):
            if no:
                percorrer(no.esquerda)
                percorrer(no.direita)
                resultado.append(no.valor)

        percorrer(self.raiz)
        return resultado

    def largura(self):
        if self.raiz is None:
            return []

        resultado = []
        fila = deque([self.raiz])

        while fila:
            atual = fila.popleft()
            resultado.append(atual.valor)

            if atual.esquerda:
                fila.append(atual.esquerda)
            if atual.direita:
                fila.append(atual.direita)

        return resultado

    def altura(self):
        def calcular(no):
            if no is None:
                return -1
            return 1 + max(calcular(no.esquerda), calcular(no.direita))

        return calcular(self.raiz)

    def contar_nos(self):
        def contar(no):
            if no is None:
                return 0
            return 1 + contar(no.esquerda) + contar(no.direita)

        return contar(self.raiz)

    def contar_folhas(self):
        def contar(no):
            if no is None:
                return 0
            if no.esquerda is None and no.direita is None:
                return 1
            return contar(no.esquerda) + contar(no.direita)

        return contar(self.raiz)

    def imprimir(self):
        def mostrar(no, nivel=0, prefixo="Raiz: "):
            if no is not None:
                print(" " * (nivel * 4) + prefixo + str(no.valor))
                mostrar(no.esquerda, nivel + 1, "E--- ")
                mostrar(no.direita, nivel + 1, "D--- ")

        mostrar(self.raiz)


class ArvoreBST:
    """Árvore Binária de Busca.

    Regra:
    - valores menores ficam à esquerda;
    - valores maiores ficam à direita;
    - valores repetidos são ignorados.
    """

    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        novo = No(valor)

        if self.raiz is None:
            self.raiz = novo
            return

        atual = self.raiz

        while True:
            if valor < atual.valor:
                if atual.esquerda is None:
                    atual.esquerda = novo
                    return
                atual = atual.esquerda
            elif valor > atual.valor:
                if atual.direita is None:
                    atual.direita = novo
                    return
                atual = atual.direita
            else:
                print(f"Valor {valor} já existe na árvore.")
                return

    def buscar(self, valor):
        atual = self.raiz
        comparacoes = 0

        while atual is not None:
            comparacoes += 1

            if valor == atual.valor:
                return True, comparacoes
            if valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita

        return False, comparacoes

    def caminho_busca(self, valor):
        atual = self.raiz
        caminho = []

        while atual is not None:
            caminho.append(atual.valor)

            if valor == atual.valor:
                return caminho
            if valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita

        return caminho

    def pre_ordem(self):
        resultado = []

        def percorrer(no):
            if no:
                resultado.append(no.valor)
                percorrer(no.esquerda)
                percorrer(no.direita)

        percorrer(self.raiz)
        return resultado

    def em_ordem(self):
        resultado = []

        def percorrer(no):
            if no:
                percorrer(no.esquerda)
                resultado.append(no.valor)
                percorrer(no.direita)

        percorrer(self.raiz)
        return resultado

    def pos_ordem(self):
        resultado = []

        def percorrer(no):
            if no:
                percorrer(no.esquerda)
                percorrer(no.direita)
                resultado.append(no.valor)

        percorrer(self.raiz)
        return resultado

    def largura(self):
        if self.raiz is None:
            return []

        resultado = []
        fila = deque([self.raiz])

        while fila:
            atual = fila.popleft()
            resultado.append(atual.valor)

            if atual.esquerda:
                fila.append(atual.esquerda)
            if atual.direita:
                fila.append(atual.direita)

        return resultado

    def altura(self):
        def calcular(no):
            if no is None:
                return -1
            return 1 + max(calcular(no.esquerda), calcular(no.direita))

        return calcular(self.raiz)

    def contar_nos(self):
        def contar(no):
            if no is None:
                return 0
            return 1 + contar(no.esquerda) + contar(no.direita)

        return contar(self.raiz)

    def contar_folhas(self):
        def contar(no):
            if no is None:
                return 0
            if no.esquerda is None and no.direita is None:
                return 1
            return contar(no.esquerda) + contar(no.direita)

        return contar(self.raiz)

    def menor_valor(self, no):
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

    def remover(self, valor):
        self.raiz = self._remover_recursivo(self.raiz, valor)

    def _remover_recursivo(self, no, valor):
        if no is None:
            return no

        if valor < no.valor:
            no.esquerda = self._remover_recursivo(no.esquerda, valor)
        elif valor > no.valor:
            no.direita = self._remover_recursivo(no.direita, valor)
        else:
            if no.esquerda is None and no.direita is None:
                return None
            if no.esquerda is None:
                return no.direita
            if no.direita is None:
                return no.esquerda

            sucessor = self.menor_valor(no.direita)
            no.valor = sucessor.valor
            no.direita = self._remover_recursivo(no.direita, sucessor.valor)

        return no

    def imprimir(self):
        def mostrar(no, nivel=0, prefixo="Raiz: "):
            if no is not None:
                print(" " * (nivel * 4) + prefixo + str(no.valor))
                mostrar(no.esquerda, nivel + 1, "E--- ")
                mostrar(no.direita, nivel + 1, "D--- ")

        mostrar(self.raiz)


if __name__ == "__main__":
    print("\nÁrvore Binária Comum")
    arvore = ArvoreBinaria()
    for valor in [10, 20, 30, 40, 50, 60, 70]:
        arvore.inserir(valor)
    arvore.imprimir()
    print("Pré-ordem:", arvore.pre_ordem())
    print("Em-ordem:", arvore.em_ordem())
    print("Pós-ordem:", arvore.pos_ordem())
    print("Largura:", arvore.largura())
    print("Altura:", arvore.altura())

    print("\nBST")
    bst = ArvoreBST()
    for valor in [50, 30, 70, 20, 40, 60, 80]:
        bst.inserir(valor)
    bst.imprimir()
    print("Em-ordem:", bst.em_ordem())
    print("Busca 60:", bst.buscar(60))
    print("Caminho 60:", bst.caminho_busca(60))
    bst.remover(70)
    print("Após remover 70:")
    bst.imprimir()
