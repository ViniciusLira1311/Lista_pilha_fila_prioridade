from lista_ligada import LinkedList

class Pilha:
    def __init__(self):
        self.pilha = LinkedList()
    
    def push(self, valor):
        self.pilha.inserir_fim(valor)
    
    def pop(self):
        self.pilha.remove_indice(0)
    
    def search(self, item):
        self.pilha.procura(item)



