# 8 - Diseña un programa que, dado un número real que debe representar la calificación numérica de un examen,
#  proporcione la calificación cualitativa correspondiente al número dado. La calificación cualitativa será una de las siguientes:
# «Suspenso» (nota menor que 5), «Aprobado» (nota mayor o igual que 5, pero menor que 7), 
# «Notable» (nota mayor o igual que 7, pero menor que 9), 
# «Sobresaliente» (nota mayor o igual que 9, pero menor que 10), 
# «Matrícula de Honor» (nota 10). «Suspenso» (nota menor que 5), 
# «Aprobado» (nota mayor o igual que 5, pero menor que 7), 
# «Notable» (nota mayor o igual que 7, pero menor que 9),
#  «Sobresaliente» (nota mayor o igual que 9, pero menor que 10), 
# «Matrícula de Honor» (nota 10).#

grade = float(input("Ingrese la calificación numérica del examen (0-10): "))
if 0 <= grade < 5:
    print("Suspenso")
elif 5 <= grade < 7:
    print("Aprobado")
elif 7 <= grade < 9:
    print("Notable")
elif 9 <= grade < 10:
    print("Sobresaliente")
elif grade == 10:
    print("Matrícula de Honor")
else:
    print("Error: Calificación fuera de rango.")