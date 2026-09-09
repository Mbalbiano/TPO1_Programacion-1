import random

def crear_matriz():
    """Esta funcion crea una matriz de 5x5 y la llena de ceros.
No requiere de ningun parametro para ser ejecutada.
El jugador no sera capaz de ver esta matriz en la version final.
Esta funcion devuelve la matriz 5x5 llena de ceros."""
    matriz = []
    for i in range(5):
        fila = []
        for j in range(5):
            fila.append(0)
        matriz.append(fila)
    return matriz

def mostrar_matriz(matriz):
    """Esta funcion muestra la matriz creada previamente con la funcion |crear_matriz()|.
Requiere del parametro de matriz (La creada anteriormente) para funcionar.
Esta funcion no es final y solo es para que el desarrollador prueba la sala.
Esta funcion no devuelve nada."""
    for i in range(len(matriz)):
        print(matriz[i])

def crear_mapa():
    """Esta funcion crea una matriz 5x5 y la llena de ceros.
No requiere de ningun parametro para ser ejecutada.
El jugador sera capaz de ver esta matriz en la version final.
Esta funcion devuelve la matriz 5x5 llena de ceros."""
    mapa = []
    for i in range(5):
        fila = []
        for j in range(5):
            fila.append(0)
        mapa.append(fila)
    return mapa

def mostrar_mapa(mapa):
    """Esta funcion muestra la matriz 5x5 creada anteriormente.
Requiere de el parametro matriz para ser ejecutada.
Esta funcion no devuelve nada."""
    for i in range(len(mapa)):
        print(mapa[i])
        
def eleccion():
    """Esta funcion le da al usuario las elecciones de a que coordenadas desea disparar.
No requiere de ningun parametro.
Esta funcion devuelve 2 variables de tipo int que el usuario escribio"""
    eleccion_1 = int(input("Ingrese la primera coordena a la que desea disparar: "))
    while eleccion_1 >5 or eleccion_1 <=0:
        eleccion_1 = int(input("Coordenada inexsitente, eliga otra vez: "))
    eleccion_2 = int(input("Ingrese la segunda coordena a la que desea disparar: "))
    while eleccion_2 >5 or eleccion_2 <=0:
        eleccion_2 = int(input("Coordenada inexsitente, eliga otra vez: "))
    return eleccion_1,eleccion_2
        
def actualizar(mapa):
    """Esta funcion crea 3 variables que cambian dentro de la misma para generar datos que se mostrarran al usuario. Ademas genera un bucle for para que el usuario intente encontrar los barcos
disparando. Para que el jugador eliga las coordenadas a las que quiere disparar se llama a la funcion eleccion() dentro de esta funcion.
Esta funcion tambien muestra la matriz llena de ceros (Creada anteriormente con la funcion crear_mapa()). por ultimo esta funcion muestra la cantidad de barcos restantes, hundidos y disparos
disponibles.
Esta funcion necesita la matriz 5x5 llena de ceros.
Esta funcion devuelve un int 1 o -1."""
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
    """Esta funcion genera, de manera alegatoria, la posicion de los barcos y verifica que ninguno este pegado a otro.
Necesita como parametro la matriz 5x5 que no se le muestra al jugador, es decir la creado por la funcion generar_matriz().
Esta funcion devuelve un int tipo 1 o -1"""
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

matriz = crear_matriz()
barcos = generar_barcos(matriz)
while barcos ==-1:
    chequeo = crear_matriz()
    barcos = generar_barcos(chequeo)
mostrar_matriz(barcos) #Borrar en la entrega final, solo sirve para ver donde se posicionan los barcos, el jugador no tendria que poder verlo


print("Su objetivo es derribar a los 3 barcos escondidos en este mapa de 5x5 elementos")
print("Las A marcaran sus fallos, donde hay agua, y las X marcaran sus aciertos")
mapa = crear_mapa()
actualizar = actualizar(mapa)
if actualizar ==-1:
    print("--PERDIO--") #Decidir que pasa si el jugador pierde