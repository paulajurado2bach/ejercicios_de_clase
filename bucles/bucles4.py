'''2. Suma de números del 1 al 100
Escribe un programa que calcule la suma de todos 
los números del 1 al 100 utilizando un bucle for.'''

acumulador = 0 
for indice in range(1,101): 
    acumulador = acumulador + indice
print("El sumatorio de los 100 primeros números es:", acumulador)
    