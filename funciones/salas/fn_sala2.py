import random

def crear_matriz():
    matriz = []
    for i in range(5):
        fila = []
        for j in range(5):
            fila.append(0)
        matriz.append(fila)
    return matriz

def crear_mapa():
    mapa = []
    for i in range(5):
        fila = []
        for j in range(5):
            fila.append(0)
        mapa.append(fila)
    return mapa

def mostrar_mapa(mapa):
    for i in range(len(mapa)):
        print(mapa[i])
        
def eleccion():
    eleccion_1 = int(input("Ingrese la primera coordena a la que desea disparar: "))
    while eleccion_1 >5 or eleccion_1 <=0:
        eleccion_1 = int(input("Coordenada inexsitente, eliga otra vez: "))
    eleccion_2 = int(input("Ingrese la segunda coordena a la que desea disparar: "))
    while eleccion_2 >5 or eleccion_2 <=0:
        eleccion_2 = int(input("Coordenada inexsitente, eliga otra vez: "))
    return eleccion_1,eleccion_2
        
def actualizar(mapa,barcos):
    disparos = 5
    hundidos = 0
    restantes = 3
    print("Dispone de",disparos,"disparos")
    for i in range(disparos):
        mostrar_mapa(mapa)
        eleccion_1,eleccion_2 = eleccion()
        if barcos[eleccion_1-1][eleccion_2-1] == 2:
            print("Esta posicion ya fue intentada anteriormente, eliga otra")
            eleccion_1,eleccion_2 = eleccion()
        if barcos[eleccion_1-1][eleccion_2-1] == 1:
            print("¡IMPACTO! Barco hundido")
            mapa[eleccion_1-1][eleccion_2-1] = "X" #se pueden cambiar la X por alguna otra cosa
            hundidos +=1
            restantes -=1
        else:
            print("AGUA")
            mapa[eleccion_1-1][eleccion_2-1] = "A" #se pueden cambiar la A por alguna otra cosa
        disparos -= 1
        print("Barcos hundidos:",hundidos)
        print("Barcos restantes:",restantes)
        print("Disparos restantes",disparos)
        barcos[eleccion_1-1][eleccion_2-1] = 2
        if restantes == 0:
            print("--FELICIDADES--")
            print("Hundio todos los barcos")
            return 1
    return -1
    
        
def generar_barcos(matriz):
    barco1_pos1 = random.randint(0, 4)
    barco1_pos2 = random.randint(0, 4)
    matriz[barco1_pos1][barco1_pos2] = 1
    if barco1_pos1 - 2 >=0:
        matriz[barco1_pos1-random.randint(2,4)][barco1_pos2] = 1
    elif barco1_pos1 + 2 <= 5:
        matriz[barco1_pos1-random.randint(2,4)][barco1_pos2] = 1
    if barco1_pos1 - 2 >= 0:
        matriz[barco1_pos1][barco1_pos2-random.randint(2,4)] = 1
    elif barco1_pos2 + 2 <= 5:
        matriz[barco1_pos1][barco1_pos2-random.randint(2,4)] = 1
    try:
        if matriz[barco1_pos1+1][barco1_pos2] == 1 or matriz[barco1_pos1-1][barco1_pos2] == 1 or matriz[barco1_pos1][barco1_pos2+1] == 1 or matriz[barco1_pos1][barco1_pos2-1] == 1:
            return -1
    except:
        return -1
    return matriz
