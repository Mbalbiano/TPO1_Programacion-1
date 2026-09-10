from funciones.gestion_usuarios.contraseñas import validar_contraseñ

contraseña = "Unodos34%"
usuario = "Jugador"
U_usuario = input("Ingrese el nombre del jugador: ")
while U_usuario != usuario:
    U_usuario = input("Nombre de jugador incorrecto, vuelva a intentarlo: ")
contra_usuario = input("Ingrese la contraseña: ")
while contra_usuario != contraseña:
    contra_usuario = input("ERROR -- Ingrese nuevamente la contraseña: ")
validar = validar_contraseña(contraseña,contra_usuario)
if validar == True:
    menu()
