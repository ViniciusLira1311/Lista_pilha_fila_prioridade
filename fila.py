from lista_ligada import LinkedList

class fila:
    def __init__(self):
        self.fila = LinkedList()
    
    def enfila(self, valor):
        self.fila.inserir_fim(valor)
    
    def desenfila(self):
        self.fila.remove_indice(0)
    
    def search(self, item):
        self.fila.procura(item)
