import random

def crear_matriz():
    matriz = []
    for i in range(5):
        fila = []
        for j in range(5):
            fila.append(0)
        matriz.append(fila)
    return matriz

def generar_barcos(matriz):
    barco1_pos1 = random.randint(0, 4)
    barco1_pos2 = random.randint(0, 4)
    matriz[barco1_pos1][barco1_pos2] = 1
    if barco1_pos1 - 2 >=0:
        matriz[barco1_pos1-2][barco1_pos2] = 1
    else:
        matriz[barco1_pos1+2][barco1_pos2] = 1
    if barco1_pos1 -2 >= 0:
        matriz[barco1_pos1][barco1_pos2-2] = 1
    else:
        matriz[barco1_pos1][barco1_pos2+2] = 1
    return matriz
    
def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])


