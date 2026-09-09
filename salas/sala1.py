#Ahorcado - Francesco Balbiano
import random
from funciones.salas.fn_sala1 import * #importa todas las funciones que el juego necesita para funcionar

"""
Funcion juego_ahorcado
Inicia el juego del ahorcado, en el cual el jugador debera de adivinar una palabra aleatoria ingresando una letra a la vez.
Si la letra no se encuentra dentro de la palabra aleatoria, se le resta un intento. Si se queda sin intentos, se le pregunta si quiere intentarlo de nuevo o volver al menu principal.
En caso de ganar el juego, se lo felicita y retorna al menu principal, ahora con la primera sala completa 
"""


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

    #Logica del juego - Si el jugador se queda sin intentos, sale del bucle
    while error_max != 0:

        print (lista_palabra,"Son",len(palabra_seleccionada),"letras")
        
        #Ingreso y validacion de input
        validacion = False
        while validacion == False:
            letra = input("Ingrese una sola letra: ")
            validacion = validacion_input(letra, letras_usadas)

        #Actualiza la lista que muestra al jugador la posicion y cantidad de letras adivinadas. 
        #Si no adivino ninguna letra, se le resta un intento 
        lista_palabra, error_max = apariciones_letra_en_palabra(letra,palabra_seleccionada,lista_palabra,error_max)
        
        #Verifica si el jugador adivino la palabra
        gg = verif_gg(lista_palabra,palabra_seleccionada) 
        if gg == True:
            return gg #Retorna la sala de escape como completada

        print ("===================================")
        print ("Intentos restantes:",error_max)
        print ("Letras ya usadas:",letras_usadas)
        print ("===================================")

    #Si el jugador se queda sin intentos, le preguntamos que quiere hacer
    opcion = gameover()
    if opcion == 1: #hacemos que la funcion se llame a si misma para que lo vuelva a intentar
        juego_ahorcado()
    else: 
        return False #Retorna la sala de escape como incompleta

# Revisar luego logica del gg. No podemos permitir que si el jugador ya gano esta sala y quiere volver a jugarla pierda su "Marca" de victoria y la sala
# aparezca nuevamente como incompleta en caso de perder. ¿quizas podria hacer que simplemente no retorne false?. La solucion depende de como se vea el resto del codigo :p
    
