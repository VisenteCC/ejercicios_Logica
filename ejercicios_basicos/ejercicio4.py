#Solicitar al usuario que ingrese la base y la altura de un rectángulo y mostrar el área en pantalla.
#area = base * altura

while True:
    try:
        base = float(input("Porfavor, Ingrese la base del rectángulo: "))
        break
    except ValueError:
        print("Porfavor, ingrese números validos para la base")

while True:
    try:
        altura = float(input("Porfavor, Ingrese la altura del rectángulo: "))
        break
    except ValueError:
        print("Porfavor, ingrese números validos para la altura")

area = base * altura
print(f"Su area es: {area}m²")



# while True:
#     try:
#         base, altura = map(float, input("Ingrese la base y altura del rectángulo separadas por espacio: ").split())
#         break
#     except ValueError:
#         print("Por favor, ingrese dos números válidos separados por espacio.")
# area = base * altura
# print(f"El área del rectángulo es: {area:.2f} m²")
# 
# ESTA SERIA UNA FORMA MAS COMPACTA DE HACERLO PERO DEBERIA SABER BIEN COMO 
# FUNCIONA EL MAP Y EL SPLIT