class TabelaHashEncadeamento:
    def __init__(self, tamanho=10):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]
        self.quantidade = 0

    def funcao_hash(self, chave):
        return hash(chave) % self.tamanho

    def inserir(self, chave, valor):
        indice = self.funcao_hash(chave)
        balde = self.tabela[indice]

        for i, (k, v) in enumerate(balde):
            if k == chave:
                balde[i] = (chave, valor)
                return

        balde.append((chave, valor))
        self.quantidade += 1

    def buscar(self, chave):
        indice = self.funcao_hash(chave)
        balde = self.tabela[indice]

        for k, v in balde:
            if k == chave:
                return v
        return None

    def remover(self, chave):
        indice = self.funcao_hash(chave)
        balde = self.tabela[indice]

        for i, (k, v) in enumerate(balde):
            if k == chave:
                del balde[i]
                self.quantidade -= 1
                return True
        return False

    def fator_carga(self):
        return self.quantidade / self.tamanho

    def imprimir(self):
        for i, balde in enumerate(self.tabela):
            print(i, "->", balde)


class TabelaHashSondagemLinear:
    def __init__(self, tamanho=10):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho
        self.REMOVIDO = object()
        self.quantidade = 0

    def funcao_hash(self, chave):
        return hash(chave) % self.tamanho

    def inserir(self, chave, valor):
        indice = self.funcao_hash(chave)
        primeiro_removido = None

        for tentativa in range(self.tamanho):
            pos = (indice + tentativa) % self.tamanho
            item = self.tabela[pos]

            if item is self.REMOVIDO:
                if primeiro_removido is None:
                    primeiro_removido = pos

            elif item is None:
                destino = primeiro_removido if primeiro_removido is not None else pos
                self.tabela[destino] = (chave, valor)
                self.quantidade += 1
                return True

            else:
                k, v = item
                if k == chave:
                    self.tabela[pos] = (chave, valor)
                    return True

        if primeiro_removido is not None:
            self.tabela[primeiro_removido] = (chave, valor)
            self.quantidade += 1
            return True

        return False

    def buscar(self, chave):
        indice = self.funcao_hash(chave)

        for tentativa in range(self.tamanho):
            pos = (indice + tentativa) % self.tamanho
            item = self.tabela[pos]

            if item is None:
                return None

            if item is not self.REMOVIDO:
                k, v = item
                if k == chave:
                    return v

        return None

    def remover(self, chave):
        indice = self.funcao_hash(chave)

        for tentativa in range(self.tamanho):
            pos = (indice + tentativa) % self.tamanho
            item = self.tabela[pos]

            if item is None:
                return False

            if item is not self.REMOVIDO:
                k, v = item
                if k == chave:
                    self.tabela[pos] = self.REMOVIDO
                    self.quantidade -= 1
                    return True

        return False

    def fator_carga(self):
        return self.quantidade / self.tamanho

    def imprimir(self):
        for i, item in enumerate(self.tabela):
            if item is self.REMOVIDO:
                print(i, "-> REMOVIDO")
            else:
                print(i, "->", item)


if __name__ == "__main__":
    print("Encadeamento separado")
    h = TabelaHashEncadeamento(10)
    for x in [25, 35, 14, 24, 10, 30, 45]:
        h.inserir(x, f"valor-{x}")
    h.imprimir()
    print("Busca 24:", h.buscar(24))
    print("Remove 35:", h.remover(35))
    h.imprimir()

    print("\nSondagem linear")
    s = TabelaHashSondagemLinear(10)
    for x in [25, 35, 14, 24, 10, 30, 45]:
        s.inserir(x, f"valor-{x}")
    s.imprimir()
    print("Busca 45:", s.buscar(45))
    print("Remove 35:", s.remover(35))
    s.imprimir()
