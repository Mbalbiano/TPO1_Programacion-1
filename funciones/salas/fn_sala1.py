#fn sala 1 - Francesco Balbiano

"""
Funcion validacion_input
- La funcion recibe la letra a validar ingresada previamente por el usuario y una lista que almacena las letras ya usadas por el usuario para su uso posterior.
  usando estos parametros, se realizan las siguientes validaciones:
  
  1) Se valida si solo se ingreso un caracter
  2) Se valida si se introdujeron numeros en vez de letras
  3) Se valida si el caracter ingresado ya se ha usado antes
  
- De resutar alguna de estas validaciones incorrectas, retorna False. En caso contrario, retorna True y añade la letra a la lista de las ya usadas
"""
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

"""
Funcion palabra_visible_jugador
- La funcion recibe el parametro palabra_seleccionada, la cual es la palabra que el jugador debera de adivinar.
  Usando este parametro, la funcion crea una lista mediante la cual el jugador podra visibilizar la cantidad de caracteres que posee la palabra.
  Retorna la lista para su posterior uso
"""
def palabra_visible_jugador (palabra_seleccionada):
    lista = []
    for i in range (len(palabra_seleccionada)):
        lista.append("_") #Informacion visible para el jugador sobre la palabra
    return lista

"""
Funcion apariciones_letra_en_palabra
- La funcion se encarga de determinar cuantas veces aparece la letra ingresada por el jugador (letra) dentro de la palabra que este debe adivinar (palabra_seleccionada).
  Luego, hace visible esta informacion al jugador mediante el reemplazo de los "_" dentro de la lista creada anteriormente por palabra_visible_jugador (lista).
  
- En caso de que la letra ingresasa no coincidiese, la lista no se modifica y se le resta un intento al jugador.
"""
def apariciones_letra_en_palabra (letra, palabra_seleccionada,lista,intentos):
    caracteres_reemplazados = 0
    for posicion, caracter in enumerate (palabra_seleccionada):
        if caracter == letra:
            lista[posicion] = letra
            caracteres_reemplazados += 1
    if caracteres_reemplazados < 1:
        intentos -= 1

    return lista,intentos

"""
Funcion verif_gg
- Valida que en la lista mediante la cual se le muestra la palabra que el jugador debe de adivinar (lista), no se encuentren guiones bajos.
  de ser este el caso, muestra al jugador un mensaje en el cual se le indica su victoria, retornando True.
  
- En caso de que sigan habiendo guiones bajos en la lista, es decir, que el jugador no haya ganado, no hace nada.
"""
def verif_gg(lista,palabra_seleccionada):
      if "_" not in lista:
        print("===================================")
        print("¡Ganaste! La palabra era:", palabra_seleccionada)
        print("===================================")
        return True

"""
Funcion gameover
- Si el jugador se queda sin intentos, se llama esta funcion, en la que se le da a elegir al jugador entre dos opciones:
  1) Volver a intentar          | Retorna 1 y vuelve a iniciar el juego
  2) Regresar al menú principal | Retorna 2 y regresa al menu principal
"""
def gameover():
    print ("""
===========
 GAME OVER
===========
¿Que quiere hacer?
1) Volver a intentar
2) Regresar al menú principal
        """)
    opcion = input("Seleccione una opción (1/2): ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 2:
        print("Seleccione una opcion valida")
        opcion = input("Seleccione una opción (1/2): ")
    return int(opcion)