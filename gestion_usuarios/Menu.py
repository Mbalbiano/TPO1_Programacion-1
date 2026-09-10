from funciones.gestion_usuarios.contrasenas import *
from salas.sala1 import juego_ahoracado
from funciones.salas.fn_sala2 import jugar_batalla

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
        completada = juego_ahorcado()
        if completada:
            print("¡Sala 1 completada!")
            jugar_batalla()
        else:
            print("Volviste al menú sin completar la sala.")
            menu()
    elif op ==2:
        cambiar_contraseña()
    else:
        print("--Sesion cerrada--")
        
menu()
