import random
from funciones.salas.fn_sala2 import *



def juego_batalla_naval():
    # Generar tablero interno
    matriz = crear_matriz()
    barcos = generar_barcos(matriz)
    while barcos == -1:
        chequeo = crear_matriz()
        barcos = generar_barcos(chequeo)

    mapa = crear_mapa()
    
    # DATOS DEL JUGADOR
    disparos = 5
    hundidos = 0
    restantes = 3

    print("""
░░░░░░░░  ░░░░░░░   ░░░░░░░░░   ░░░░░░░   ░░        ░░        ░░░░░░░ 
▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒  ▒▒        ▒▒       ▒▒▒▒▒▒▒▒▒
▓▓    ▓▓  ▓▓    ▓▓     ▓▓      ▓▓     ▓▓  ▓▓        ▓▓       ▓▓     ▓▓
███████   ████████     ██      █████████  ██        ██       █████████
██    ██  ██    ██     ██      ██     ██  ██        ██       ██     ██
████████  ██    ██     ██      ██     ██  ████████  ████████ ██     ██

░░      ░░  ░░░░░░░░  ░░        ░░  ░░░░░░░░  ░░       
▒▒▒▒    ▒▒  ▒▒▒▒▒▒▒▒  ▒▒        ▒▒  ▒▒▒▒▒▒▒▒  ▒▒       
▓▓▓▓▓   ▓▓  ▓▓    ▓▓  ▓▓        ▓▓  ▓▓    ▓▓  ▓▓       
██ ▓▓▓  ██  ████████  ██        ██  ████████  ██       
██   ▓▓ ██  ██    ██   ██      ██   ██    ██  ██       
██    ████  ██    ██    ████████    ██    ██  ████████ 


╷ ╷╭─╮╭─╴╷ ╷╷╭╮╷╭─╴╶┬╴╭─╮╭╮╷   ╶┬╮╭─╴   ╷╭╮╷╭─╴ 
│╷│├─┤│  ├─┤││╰┤│╶╮ │ │ ││╰┤    │││     ││╰┤│   
╰┴╯╵ ╵╰─╴╵ ╵╵╵ ╵╰─╯ ╵ ╰─╯╵ ╵   ╶┴╯╰─╴   ╵╵ ╵╰─╴.                                                        
    """) #logo del juego

    # Logica del juego - Si el jugador se queda sin disparos, sale del bucle
    while disparos != 0:

        mostrar_mapa(mapa)
        
        # Ingreso y validacion de coordenadas
        eleccion_1, eleccion_2 = eleccion()
        
        if barcos[eleccion_1-1][eleccion_2-1] == 2:
            print("Esta posición ya fue intentada anteriormente, elija otra.")
            eleccion_1, eleccion_2 = eleccion()

        # Actualiza el mapa que muestra al jugador la posición atacada.
        if barcos[eleccion_1-1][eleccion_2-1] == 1:
            print("\n¡IMPACTO! Barco hundido")
            mapa[eleccion_1-1][eleccion_2-1] = "X"
            hundidos += 1
            restantes -= 1
        else:
            print("\nAGUA")
            mapa[eleccion_1-1][eleccion_2-1] = "A"

        barcos[eleccion_1-1][eleccion_2-1] = 2
        disparos -= 1

        print("===================================")
        print("Disparos restantes:", disparos)
        print("Barcos hundidos:", hundidos)
        print("Barcos restantes:", restantes)
        print("===================================")

        # Verifica si el jugador adivinó todos los barcos
        if restantes == 0:
            print("\n--FELICIDADES--")
            print("¡Hundió todos los barcos!")
            return True # Retorna la sala de escape como completada

    # Si el jugador se queda sin disparos, le preguntamos qué quiere hacer
    opcion = gameover()
    if opcion == 1: # Hacemos que la función se llame a sí misma para que lo vuelva a intentar
        juego_batalla_naval()
    else:
        return False # Retorna la sala de escape como incompleta
