# pedir al usuario por el numero de la tabla 
print("dime el número de la tabla de multiplicar")
num_tabla = int(input())
indice = 1
 
while(indice <= 10):
     resultado = num_tabla * indice
     print(indice, "x",num_tabla,"=",resultado)
     indice = indice + 1
