#Ahorcado - Francesco Balbiano
import random, re
from funciones.salas.fn_sala1 import *

def juego_ahorcado ():
    palabras_juego = ["timba","blackjack","dados","ruleta","fichas","poker","cartas","apuestas","noche","slots","tragaperras","casino"]
    palabra_seleccionada = (random.choice(palabras_juego))
    lista_palabra = palabra_visible_jugador(palabra_seleccionada)
    
    #DATOS DEL JUGADOR
    error_max = 5
    letras_usadas = []

    print("""
    ░░      ░░░  ░░░░  ░░░      ░░░       ░░░░      ░░░░      ░░░       ░░░░      ░░
    ▒  ▒▒▒▒  ▒▒  ▒▒▒▒  ▒▒  ▒▒▒▒  ▒▒  ▒▒▒▒  ▒▒  ▒▒▒▒  ▒▒  ▒▒▒▒  ▒▒  ▒▒▒▒  ▒▒  ▒▒▒▒  ▒
    ▓  ▓▓▓▓  ▓▓        ▓▓  ▓▓▓▓  ▓▓       ▓▓▓  ▓▓▓▓▓▓▓▓  ▓▓▓▓  ▓▓  ▓▓▓▓  ▓▓  ▓▓▓▓  ▓
    █        ██  ████  ██  ████  ██  ███  ███  ████  ██        ██  ████  ██  ████  █
    █  ████  ██  ████  ███      ███  ████  ███      ███  ████  ██       ████      ██
                                                            
    ╷ ╷╭─╮╭─╴╷ ╷╷╭╮╷╭─╴╶┬╴╭─╮╭╮╷   ╶┬╮╭─╴   ╷╭╮╷╭─╴ 
    │╷│├─┤│  ├─┤││╰┤│╶╮ │ │ ││╰┤    │││     ││╰┤│   
    ╰┴╯╵ ╵╰─╴╵ ╵╵╵ ╵╰─╯ ╵ ╰─╯╵ ╵   ╶┴╯╰─╴   ╵╵ ╵╰─╴.                                                        
    """) #logo del juego

    #Logica del juego
    while error_max != 0:

        print (lista_palabra,"Son",len(palabra_seleccionada),"letras")
        letra = input("Ingrese una sola letra: ")
        validacion = validacion_input(letra,letras_usadas) #Funcion para validacion del imput del usuario

        while validacion == False:
            letra = input("Ingrese una sola letra: ")
            validacion = validacion_input(letra,letras_usadas)

        lista_palabra, error_max=apariciones_letra_en_palabra(letra,palabra_seleccionada,lista_palabra,error_max)
        gg=verif_gg(lista_palabra,palabra_seleccionada) #Verifica si el jugador adivino la palabra

        #Cuando se comete un error, se le resta 1 a la variable. cuando se queda sin errores sale del bucle
        print ("===================================")
        print ("Intentos restantes:",error_max)
        print ("Letras ya usadas:",letras_usadas)
        print ("===================================")

    #Si el jugador se queda sin intentos, le preguntamos que quiere hacer
    opcion = gameover()
    if opcion == 1: #hacemos que la funcion se llame a si misma para que lo vuelva a intentar
        juego_ahorcado()
