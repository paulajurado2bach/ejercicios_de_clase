'''3. Acceso por Contraseña
Escribe un programa que le pida al usuario ingresar un nombre de usuario y 
una contraseña. Si el nombre de usuario es "admin" y la contraseña es "1234",
el programa debe mostrar "Acceso concedido". Si no, debe mostrar "Acceso denegado". 
Este tipo de programa se utiliza en muchos sitios web y sistemas para controlar el 
acceso.'''

# Ejercicio 3

USUARIO_BBDD = "admin" 
PASSWORD_BBDD = 1234

print("Escribe tu nombre de usuario")
usuario = input()
print("EScribe tu contraseña")
password = int(input())
if(USUARIO_BBDD == usuario) and (PASSWORD_BBDD == password):
    print("acceso concedido")
else:
    print("acceso denegado")
