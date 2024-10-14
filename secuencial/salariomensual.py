# Esto es un programa pra el cálculo del salario mensual de una persona
print("¿cuántas horas has trabajado en la semana?")
horas = int(input())
print("dime lo que cobras por horas")
salario = float(input())
salariomensual = horas * salario * 4 
print("tu sueldo mensual es: ", salariomensual, "€")
