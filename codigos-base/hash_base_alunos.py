class TabelaHashEncadeamento:
    def __init__(self, tamanho=10):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]

    def funcao_hash(self, chave):
        # TODO: transformar a chave em um indice valido
        pass

    def inserir(self, chave, valor):
        # TODO: calcular indice, verificar se chave existe e inserir/atualizar
        pass

    def buscar(self, chave):
        # TODO: retornar o valor associado a chave ou None
        pass

    def remover(self, chave):
        # TODO: remover chave e retornar True/False
        pass

    def fator_carga(self):
        # TODO: quantidade de itens / tamanho da tabela
        pass

    def imprimir(self):
        for i, balde in enumerate(self.tabela):
            print(i, "->", balde)


class TabelaHashSondagemLinear:
    def __init__(self, tamanho=10):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho
        self.REMOVIDO = object()

    def funcao_hash(self, chave):
        # TODO: transformar a chave em indice
        pass

    def inserir(self, chave, valor):
        # TODO: inserir usando sondagem linear
        pass

    def buscar(self, chave):
        # TODO: buscar usando sondagem linear
        pass

    def remover(self, chave):
        # TODO: marcar posicao como removida
        pass

    def imprimir(self):
        for i, item in enumerate(self.tabela):
            if item is self.REMOVIDO:
                print(i, "-> REMOVIDO")
            else:
                print(i, "->", item)


if __name__ == "__main__":
    # Use este arquivo como roteiro de implementacao em sala.
    # Comece pelo encadeamento separado.
    pass
