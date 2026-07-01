# ============================================================
# Estruturas de Dados II
# Arvore Rubro-Negra - codigo base para completar em sala
# ============================================================

class NoRB:
    def __init__(self, valor, cor="VERMELHO"):
        self.valor = valor
        self.cor = cor
        self.esquerda = None
        self.direita = None
        self.pai = None


class ArvoreRubroNegra:
    VERMELHO = "VERMELHO"
    PRETO = "PRETO"

    def __init__(self):
        self.NIL = NoRB(None, self.PRETO)
        self.raiz = self.NIL

    def inserir(self, valor):
        """Insere como BST e depois chama a correcao rubro-negra."""
        novo = NoRB(valor, self.VERMELHO)
        novo.esquerda = self.NIL
        novo.direita = self.NIL

        pai = None
        atual = self.raiz

        while atual != self.NIL:
            pai = atual
            if novo.valor < atual.valor:
                atual = atual.esquerda
            elif novo.valor > atual.valor:
                atual = atual.direita
            else:
                print(f"Valor {valor} ja existe. Ignorando.")
                return

        novo.pai = pai

        if pai is None:
            self.raiz = novo
        elif novo.valor < pai.valor:
            pai.esquerda = novo
        else:
            pai.direita = novo

        self.corrigir_insercao(novo)

    def rotacao_esquerda(self, x):
        """TODO: implementar rotacao a esquerda."""
        pass

    def rotacao_direita(self, y):
        """TODO: implementar rotacao a direita."""
        pass

    def corrigir_insercao(self, z):
        """TODO: implementar os casos de correcao da insercao."""
        pass

    def em_ordem(self):
        resultado = []

        def visitar(no):
            if no != self.NIL:
                visitar(no.esquerda)
                resultado.append((no.valor, no.cor))
                visitar(no.direita)

        visitar(self.raiz)
        return resultado

    def imprimir(self):
        def mostrar(no, nivel=0, prefixo="Raiz: "):
            if no != self.NIL:
                print(" " * (nivel * 4) + prefixo + f"{no.valor} ({no.cor})")
                mostrar(no.esquerda, nivel + 1, "E--- ")
                mostrar(no.direita, nivel + 1, "D--- ")

        mostrar(self.raiz)


if __name__ == "__main__":
    rb = ArvoreRubroNegra()

    valores = [10, 20, 30, 15, 25, 5, 1]

    for valor in valores:
        print("\nInserindo:", valor)
        rb.inserir(valor)
        rb.imprimir()

    print("\nEm ordem:", rb.em_ordem())
