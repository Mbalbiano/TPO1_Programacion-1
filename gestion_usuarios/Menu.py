from funciones.gestion_usuarios.contrasenas import *
from salas.sala1 import juego_ahorcado
from salas.sala2 import jugar_batalla

def menu():
    print("Coloque el numero correspondiete a la accion que desea tomar")
    print("""
    1. Jugar a la sala_01
    2. Cambiar la contraseña
    3. Cerrar sesion""")
    op = int(input(""))
    while op !=1 and op !=2 and op !=3:
        print("""La opcion elegida no es valida, vuelva a intentar
    1. Jugar a la sala_01
    2. Cambiar la contraseña
    3. Cerrar sesion""")
        op = int(input(""))
    if op == 1:
        introduccion()
        completada = juego_ahorcado()
        if completada:
            print("¡Sala 1 completada!")
            jugar_batalla()
        else:
            print("Volviste al menú sin completar la sala.")
            menu()
    elif op ==2:
        cambiar_contraseña()
        menu()
    else:
        print("--Sesion cerrada--")
def introduccion():
    print("""Todo empezó con una mala noche de póker. Apostaste más de lo que tenías, firmaste papeles que no leíste con cuidado, y ahora Eduardo —el dueño del casino más temido de la ciudad— dice que le debes una fortuna en plata. Esta noche recibiste una carta sellada con cera negra: "Ven al casino a medianoche. O pagas tu deuda jugando mis juegos... o la pagas de otra forma."
    No tuviste opción. Cruzaste las puertas del casino "Wachington D.C.", y apenas pisaste la alfombra roja, escuchaste el cerrojo de la entrada cerrarse detrás de ti. Las luces de neón parpadean, y una voz grave resuena desde algún altavoz oculto:

    "Bienvenido, deudor. Esta casa no perdona deudas... las cobra. Tienes dos salas por delante. Supéralas, y tu deuda queda saldada. Falla, y te quedas aquí, jugando para la casa, para siempre."

    Frente a ti hay dos puertas. Ambas llevan a un juego. Ambas son tu única salida.""")

if __name__ == "__main__":
    menu()
