# ============================================================
# Estruturas de Dados II
# Arvore Rubro-Negra - versao de referencia
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
        y = x.direita
        x.direita = y.esquerda

        if y.esquerda != self.NIL:
            y.esquerda.pai = x

        y.pai = x.pai

        if x.pai is None:
            self.raiz = y
        elif x == x.pai.esquerda:
            x.pai.esquerda = y
        else:
            x.pai.direita = y

        y.esquerda = x
        x.pai = y

    def rotacao_direita(self, y):
        x = y.esquerda
        y.esquerda = x.direita

        if x.direita != self.NIL:
            x.direita.pai = y

        x.pai = y.pai

        if y.pai is None:
            self.raiz = x
        elif y == y.pai.direita:
            y.pai.direita = x
        else:
            y.pai.esquerda = x

        x.direita = y
        y.pai = x

    def corrigir_insercao(self, z):
        while z.pai is not None and z.pai.cor == self.VERMELHO:
            if z.pai == z.pai.pai.esquerda:
                tio = z.pai.pai.direita

                if tio.cor == self.VERMELHO:
                    z.pai.cor = self.PRETO
                    tio.cor = self.PRETO
                    z.pai.pai.cor = self.VERMELHO
                    z = z.pai.pai
                else:
                    if z == z.pai.direita:
                        z = z.pai
                        self.rotacao_esquerda(z)

                    z.pai.cor = self.PRETO
                    z.pai.pai.cor = self.VERMELHO
                    self.rotacao_direita(z.pai.pai)
            else:
                tio = z.pai.pai.esquerda

                if tio.cor == self.VERMELHO:
                    z.pai.cor = self.PRETO
                    tio.cor = self.PRETO
                    z.pai.pai.cor = self.VERMELHO
                    z = z.pai.pai
                else:
                    if z == z.pai.esquerda:
                        z = z.pai
                        self.rotacao_direita(z)

                    z.pai.cor = self.PRETO
                    z.pai.pai.cor = self.VERMELHO
                    self.rotacao_esquerda(z.pai.pai)

        self.raiz.cor = self.PRETO

    def buscar(self, valor):
        atual = self.raiz
        comparacoes = 0

        while atual != self.NIL:
            comparacoes += 1
            if valor == atual.valor:
                return True, comparacoes
            if valor < atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita

        return False, comparacoes

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

    for busca in [1, 25, 100]:
        encontrado, comparacoes = rb.buscar(busca)
        print(f"Busca {busca}: encontrado={encontrado}, comparacoes={comparacoes}")
