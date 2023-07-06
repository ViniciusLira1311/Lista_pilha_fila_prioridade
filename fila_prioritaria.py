from lista_ligada import LinkedList

class fila_prioritaria:
    def __init__(self):
        self.filaPrio = LinkedList()
        self.fila = LinkedList()
    def enfila(self, valor):
        if valor >= 60:
            self.filaPrio.inserir_inicio(valor)
        else:
            self.fila.inserir_inicio(valor)
    def desenfila(self):
        if self.filaPrio.esta_vazio():
            self.fila.remove(0)
        else:
            self.filaPrio.remove(0)
    
    def search(self, item):
        if self.filaPrio.esta_vazio():
            self.fila.procura(item)
        else:
            self.filaPrio.procura(item)
        