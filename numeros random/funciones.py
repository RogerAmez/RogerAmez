import random
def generar_numeros():
    lista = []
    for i in range(15):
        num=random.randint(1,50)
        lista.append(num)
    return lista

def ordenar(lista):
    return lista.sort()

def imprimir(lista):
    return print( lista)





