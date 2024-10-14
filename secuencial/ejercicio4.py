# Esto es un programa para calciular propinas 
print("dime una cantidad")
factura = int(input())
porcentaje = float(15.0)
# Realizamos la operación 
propina = factura * (porcentaje / 100)
print("la propina es", propina, "€")
