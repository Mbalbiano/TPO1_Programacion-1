# Fn para contraseñas - Francesco Balbiano; funciones ord(), chr() para encriptacion y .isalnum() para la validación sugeridas por Claude code :p
"""
===========================
 ACERCA DE ESTAS FUNCIONES
===========================

- Para estas funciones aprendi acerca de ord(), chr() y .isalnum(), las cuales NO vimos en la cursada y voy a explicar aca para que 
  si alguien de mi curso lee este codigo lo entienda correctamente y no se rompa la cabeza.
  
  En la encriptacion se usa:
  ord(): Transforma los strings a su codigo ASCII correspondiente. ej. h -> 104 (numero decimal en codigo ASCII)
  chr(): Hace lo opuesto a ord(), transformando el numero decimal en codigo ASCII a un string. ej. 64 -> @
  
  https://www.asciitable.com/ | Tabla ASCII online para que puedan visualizar mejor lo que quiero explicar
  
  En la validacion se usa:
  .isalnum(): Verifica que el string contenga unicamente caracteres alfanumericos. Si esto es asi, retorna True.
              en caso contrario, retorna False. Justamente por este motivo utilizo este metodo con not para validar si
              el string contiene caracteres especiales, a fin de mantener el codigo simple. :D
              
Saludos! - Francesco Balbiano
"""

"""
Valida el input del usuario para que cumpla los siguientes standares de seguridad:
 1) se usan los argumentos contraseña y confirmacion para validar que el usuario haya ingresado correctamente la contraseña
 2) se valida que la contraseña no tenga menos de 8 caracteres
 3) se valida que la contraseña contenga caracteres que cumplan con los siguientes requisitos:
        La contraseña debe contener por lo menos
        - Una mayuscula
        - Una minuscula
        - Un numero
        - Un caracter especial (ej: @, #, !, _)

- Si la contraseña pasa todas las validaciones de seguridad, retorna True, en caso contrario, retorna false 
"""
def validar_contraseña(contraseña,confirmacion):
    if contraseña != confirmacion: #primera validacion
        print("Las contraseñas no coinciden. Intentá de vuelta")
        return False
    elif len(contraseña) < 8: #segunda validacion
        print("La contraseña tiene menos de 8 caracteres. Intentá de vuelta")
        return False
    
    #Usamos estas variables para validar mas tarde con el if, luego de recorrer la contraseña
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    tiene_especial = False
    
    #Recorre la contraseña buscando que se cumplan los requisitos
    for caracter in contraseña:
         if caracter.isupper():          # ej: 'A', 'B', 'C'...
             tiene_mayuscula = True
         elif caracter.islower():        # ej: 'a', 'b', 'c'...
             tiene_minuscula = True
         elif caracter.isdigit():        # ej: '0', '1', '2'...
             tiene_numero = True
         elif not caracter.isalnum():
             tiene_especial = True        # ej: '@', '#', '!', '_'...
    
    #validacion
    if not tiene_mayuscula:
         print("La contraseña debe tener al menos una mayúscula. Intentá de vuelta")
         return False
    if not tiene_minuscula:
         print("La contraseña debe tener al menos una minúscula. Intentá de vuelta")
         return False
    if not tiene_numero:
         print("La contraseña debe tener al menos un número. Intentá de vuelta")
         return False
    if not tiene_especial:
         print("La contraseña debe tener al menos un carácter especial (ej: @, #, !, _). Intentá de vuelta")
         return False
    
    return True

"""
Funcion encriptar_contraseña
Recibe una contraseña ingresada por el usuario y devuelve una versión encriptada.
Recorre cada caracter, obtiene su código numérico en ASCII con ord(), le suma el desplazamiento, 
y lo vuelve a convertir en caracter con chr(), encriptando efectivamente la contraseña.
"""
def encriptar_contraseña(contraseña, desplazamiento=5):
    contraseña_encriptada = ""
 
    for caracter in contraseña:
        codigo_original = ord(caracter)              # letra -> número
        codigo_nuevo = codigo_original + desplazamiento
        caracter_encriptado = chr(codigo_nuevo)          # número -> nueva letra
        contraseña_encriptada += caracter_encriptado
 
    return contraseña_encriptada

"""
Encripta el input del usuario y lo compara con la contraseña guardada.
Si las contraseñas coinciden, retorna True. En caso contrario, retorna false
"""
def comprobar_contraseña (contraseña, contraseña_encriptada):
    input_encriptado = encriptar_contraseña(contraseña)
    
    if input_encriptado == contraseña_encriptada:
        return True
    else:
        print ("Contraseña incorrecta, intentelo nuevamente")
        return False
def cambiar_contraseña():
    nueva = input("Nueva contraseña: ")
    confirmacion = input("Confirmá la nueva contraseña: ")
    
    if validar_contraseña(nueva, confirmacion):
        nueva_encriptada = encriptar_contraseña(nueva)
        print("¡Contraseña actualizada con éxito!")
        return nueva_encriptada
    else:
        cambiar_contraseña()
     
contraseña = "Unodos34%"
usuario = "Jugador"
