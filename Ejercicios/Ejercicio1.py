# 1 - Crea un programa que lea la edad de dos personas y diga quién es más joven, la primera o la segunda. 
#Ten en cuenta que ambas pueden tener la misma edad. En tal caso, hazlo saber con un mensaje adecuado.

age1 = int(input("Ingrese la edad de la primera persona: "))
age2 = int(input("Ingrese la edad de la segunda persona: "))
if age1 < age2:
    print("La primera persona es más joven.")
elif age1 > age2:
    print("La segunda persona es más joven.")
else:
    print("Ambas personas son de la misma edad.")