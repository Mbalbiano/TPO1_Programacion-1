import random
from funciones.salas.fn_sala2 import *



def jugar_batalla():
    matriz = crear_matriz()
    barcos = generar_barcos(matriz)
    while barcos == -1:
        chequeo = crear_matriz()
        barcos = generar_barcos(chequeo)

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

    print("Su objetivo es derribar a los 3 barcos escondidos en este mapa de 5x5 elementos")
    print("Las A marcaran sus fallos, donde hay agua, y las X marcaran sus aciertos")
    
    mapa = crear_mapa()
    resultado = actualizar(mapa, barcos)
    
    if resultado == -1:
        print("\n--PERDIÓ--")
        opcion = gameover()
        if opcion == 1:
            return jugar_batalla() # Vuelve a ejecutar la función si elige reintentar
        else:
            return False # Retorna la sala como incompleta si decide volver al menú
            
    return True # Retorna la sala como completada


