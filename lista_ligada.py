from estrutura_elementar import estrutura_elementar


class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def set_proximo(self, no):
        self.proximo = no

    def get_proximo(self):
        return self.proximo


class LinkedList(estrutura_elementar):
    def __init__(self):
        self.inicio = None

    def inserir_inicio(self, valor):
        if self.inicio is None:
            self.inicio = No(valor)
        else:
            novoNo = No(valor)
            novoNo.set_proximo(self.inicio)
            self.inicio = novoNo

    def inserir_fim(self, valor):
        if self.inicio is None:
            self.inicio = No(valor)
        else:
            novoNo = No(valor)
            aux = self.inicio
            while aux.get_proximo() is not None:
                aux = aux.get_proximo()
            aux.set_proximo(novoNo)

    def esta_vazio(self) -> bool:
        if self.inicio is None:
            return True
        else:
            return False

    def remove(self, item):
        if not self.esta_vazio():
            if self.inicio.valor == item:
                self.inicio = self.inicio.get_proximo()
            else:
                anterior = None
                atual = self.inicio
                while atual is not None and atual.valor != item:
                    anterior = atual
                    atual = atual.get_proximo()
                if atual is not None:
                    anterior.set_proximo(atual.get_proximo())

    def tamanho(self) -> int:
        if self.inicio is None:
            return 0
        else:
            aux = self.inicio
            cont = 1
            while aux.get_proximo() is not None:
                aux = aux.get_proximo()
                cont += 1
            return cont

    def limpa(self):
        self.inicio = None

    def procura(self, item) -> bool:
        aux = self.inicio
        while aux is not None:
            if aux.valor == item:
                return True
            aux = aux.get_proximo()
        return False

    def indice_de(self, item):
        index = 0
        aux = self.inicio
        while aux is not None:
            if aux.valor == item:
                return index
            index += 1
            aux = aux.get_proximo()
        return -1

    def recupera_indice(self, index):
        count = 0
        aux = self.inicio
        while count < index and aux is not None:
            count += 1
            aux = aux.get_proximo()
        if count == index and aux is not None:
            return aux.valor
        else:
            return None
    def remove_indice(self, indice):
        if indice >= 0 and indice <= self.tamanho():
            self.remove(self.recupera_indice(indice))
    
        