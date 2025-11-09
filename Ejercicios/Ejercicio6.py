# 6 - Realiza un programa que pida tres números enteros y diga cuál es el mayor. No se puede usar la función max().
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))
num3 = int(input("Ingrese el tercer número entero: "))

if num1 >= num2 and num1 >= num3:
    print("El mayor es: " + str(num1))
elif num2 >= num1 and num2 >= num3:
    print("El mayor es: " + str(num2))
else:
    print("El mayor es: " + str(num3))