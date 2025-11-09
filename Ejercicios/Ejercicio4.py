# 4 - Escribir un programa que calcule el desglose mínimo en billetes y monedas
# de una cantidad exacta de euros (sin excepciones)
amount = int(input("Ingrese una cantidad entera de euros (>=0): "))  # Leer entrada del usuario

if amount < 0:
    print("Entrada no válida. Introduzca un número entero no negativo.")  # Validación de entrada
else:
    remaining = amount  # Cantidad restante por desglosar
    print("Desglose mínimo:")

    # Billetes de 500€
    if remaining >= 500:
        count = remaining // 500
        remaining = remaining % 500
        if count > 0:
            print(f"Billetes de 500€: {count}")
    else:
        count = 0

    # Billetes de 200€
    if remaining >= 200:
        count = remaining // 200
        remaining = remaining % 200
        if count > 0:
            print(f"Billetes de 200€: {count}")
    else:
        count = 0

    # Billetes de 100€
    if remaining >= 100:
        count = remaining // 100
        remaining = remaining % 100
        if count > 0:
            print(f"Billetes de 100€: {count}")
    else:
        count = 0

    # Billetes de 50€
    if remaining >= 50:
        count = remaining // 50
        remaining = remaining % 50
        if count > 0:
            print(f"Billetes de 50€: {count}")
    else:
        count = 0

    # Billetes de 20€
    if remaining >= 20:
        count = remaining // 20
        remaining = remaining % 20
        if count > 0:
            print(f"Billetes de 20€: {count}")
    else:
        count = 0

    # Billetes de 10€
    if remaining >= 10:
        count = remaining // 10
        remaining = remaining % 10
        if count > 0:
            print(f"Billetes de 10€: {count}")
    else:
        count = 0

    # Billetes de 5€
    if remaining >= 5:
        count = remaining // 5
        remaining = remaining % 5
        if count > 0:
            print(f"Billetes de 5€: {count}")
    else:
        count = 0

    # Monedas de 2€
    if remaining >= 2:
        count = remaining // 2
        remaining = remaining % 2
        if count > 0:
            print(f"Monedas de 2€: {count}")
    else:
        count = 0

    # Monedas de 1€
    if remaining >= 1:
        count = remaining // 1
        remaining = remaining % 1
        if count > 0:
            print(f"Monedas de 1€: {count}")
    else:
        count = 0