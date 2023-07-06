import sys

sys.path.append("..")

# importing
from lista_ligada import LinkedList
from pilha import Pilha
from fila import fila
from fila_prioritaria import fila_prioritaria

def test_vazio():
    lst = LinkedList()
    assert lst.esta_vazio() == True
    lst.inserir_inicio(1)
    assert lst.esta_vazio() == False
    lst.inserir_inicio(2)
    assert lst.esta_vazio() == False


def test_tamanho_1():
    lst = LinkedList()
    assert lst.tamanho() == 0
    lst.inserir_inicio(1)
    assert lst.tamanho() == 1
    lst.inserir_inicio(2)
    assert lst.tamanho() == 2


def test_tamanho_2():
    lst = LinkedList()
    assert lst.tamanho() == 0
    lst.inserir_inicio(1)
    assert lst.tamanho() == 1
    lst.inserir_inicio(2)
    assert lst.tamanho() == 2
    lst.remove(1)
    assert lst.tamanho() == 1
    lst.limpa()
    assert lst.tamanho() == 0


def test_procurar():
    lst = LinkedList()
    assert lst.procura(1) == False
    lst.inserir_inicio(1)
    assert lst.procura(1) == True
    assert lst.procura(2) == False
    lst.inserir_inicio(2)
    assert lst.procura(2) == True
    assert lst.procura(3) == False
    lst.inserir_fim(3)
    assert lst.procura(2) == True
    assert lst.procura(3) == True
    lst.remove(1)
    assert lst.procura(1) == False
    lst.limpa()
    assert lst.procura(2) == False
    assert lst.procura(1) == False
    assert lst.procura(3) == False
    assert lst.procura(4) == False


def test_indice_de():
    lst = LinkedList()
    assert lst.indice_de(1) == -1
    lst.inserir_fim(1)
    assert lst.indice_de(1) == 0
    assert lst.indice_de(2) == -1
    lst.inserir_fim(2)
    assert lst.indice_de(2) == 1
    assert lst.indice_de(3) == -1
    lst.remove(1)
    assert lst.indice_de(1) == -1
    assert lst.indice_de(2) == 0
    lst.limpa()
    assert lst.indice_de(2) == -1


def test_recupera_indice():
    lst = LinkedList()
    assert lst.recupera_indice(0) == None
    lst.inserir_fim(1)
    assert lst.recupera_indice(0) == 1
    assert lst.recupera_indice(1) == None
    lst.inserir_fim(2)
    assert lst.recupera_indice(0) == 1
    assert lst.recupera_indice(1) == 2
    assert lst.recupera_indice(2) == None
    lst.remove(1)
    assert lst.recupera_indice(0) == 2
    assert lst.recupera_indice(1) == None
    lst.limpa()
    assert lst.recupera_indice(0) == None
    assert lst.recupera_indice(1) == None
    assert lst.recupera_indice(2) == None

def test_remove_indice():
    lst = LinkedList()
    lst.inserir_fim(1)
    lst.inserir_fim(2)
    assert lst.recupera_indice(0) == 1
    lst.remove_indice(0) 
    assert lst.recupera_indice(0) == 2

def test_pilha():
    Pilha_test = Pilha()
    Pilha_test.push(1)
    Pilha_test.push(2)
    Pilha_test.push(3)
    Pilha_test.search(1) == True
    Pilha_test.pop()
    Pilha_test.search(3) == False

def test_fila():
    fila_test = fila()
    fila_test.enfila(1)
    fila_test.enfila(2)
    fila_test.enfila(3)
    fila_test.search(1) == True
    fila_test.desenfila()
    fila_test.search(1) == False

def test_fila_prio():
    fila_prio = fila_prioritaria()
    fila_prio.enfila(1)
    fila_prio.enfila(63)
    fila_prio.enfila(58)
    fila_prio.search(63) == True
    fila_prio.desenfila()
    fila_prio.search(63) == False
    fila_prio.search(58) == True
    