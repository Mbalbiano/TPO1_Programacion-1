#fn sala 1 - Francesco Balbiano

def validacion_input(letra,letras_usadas):
    
    if len(letra) != 1:
        print ("Solo debe de introducir un caracter")
        return False
    elif letra.isalpha() ==  False:
        print ("Solo debe de introducir caracteres, no numeros")
        return False
    elif letra.lower() in letras_usadas:
        print ("La letra ingresada ya ha sido usada")
        return False
    letras_usadas.append(letra.lower())
    return True, letras_usadas

def palabra_visible_jugador (palabra_seleccionada):
    lista = []
    for i in range (len(palabra_seleccionada)):
        lista.append("_") #Informacion visible para el jugador sobre la palabra
    return lista

def apariciones_letra_en_palabra (letra, palabra_seleccionada,lista,intentos):
    caracteres_reemplazados = 0
    for posicion, caracter in enumerate (palabra_seleccionada):
        if caracter == letra:
            lista[posicion] = letra
            caracteres_reemplazados += 1
    if caracteres_reemplazados < 1:
        intentos -= 1

    return lista,intentos

def verif_gg(lista,palabra_seleccionada):
      if "_" not in lista:
        print("===================================")
        print("¡Ganaste! La palabra era:", palabra_seleccionada)
        print("===================================")
        return True

def gameover():
    print ("""
===========
 GAME OVER
===========
¿Que quiere hacer?
1) Volver a intentar
2) Regresar al menú principal
        """)
    opcion = int(input("Seleccione una opción (1/2): "))
    while opcion > 2 or opcion < 0:
        print("Seleccione una opcion valida")
        opcion = input("Seleccione una opción (1/2): ")
    return opcion