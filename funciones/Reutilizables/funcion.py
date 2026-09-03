import random

def busqueda_lineal(lista,elemento_buscado):
    for i in range(len(lista)):
        if lista[i] == elemento_buscado:
            return i  
    return -1