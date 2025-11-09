#7. Realiza un programa que pida cinco números enteros y diga cuál es el mayor No se puede usar la función max().

a = int(input("Ingrese el número entero 1: "))
b = int(input("Ingrese el número entero 2: "))
c = int(input("Ingrese el número entero 3: "))
d = int(input("Ingrese el número entero 4: "))
e = int(input("Ingrese el número entero 5: "))
mayor = a
if b > mayor:
    mayor = b
if c > mayor:
    mayor = c
if d > mayor:
    mayor = d
if e > mayor:
    mayor = e

print("El mayor es: " + str(mayor))
