# 2 - Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de los lados de un triángulo.
# El programa debe determinar que tipo de triangulo es, teniendo en cuenta los siguiente:
    #Si se cumple Pitágoras entonces es triángulo rectángulo
    #Si sólo dos lados del triángulo son iguales entonces es isósceles.
    #Si los 3 lados son iguales entonces es equilátero.
    #Si no se cumple ninguna de las condiciones anteriores, es escaleno.

A = float(input("Ingrese la longitud del lado A: "))
B = float(input("Ingrese la longitud del lado B: "))
C = float(input("Ingrese la longitud del lado C: "))
# Verificar el tipo de triángulo con pitagoras y condiciones
if A**2 + B**2 == C**2 or A**2 + C**2 == B**2 or B**2 + C**2 == A**2:
    print("El triángulo es rectángulo.")
elif A == B and B == C:
    print("El triángulo es equilátero.")
elif A == B or B == C or A == C:
    print("El triángulo es isósceles.")
else:
    print("El triángulo es escaleno.")

