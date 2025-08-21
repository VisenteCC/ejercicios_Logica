#Programa que determina si una persona es mayor de edad.
while True:
    try:
        edad = int(input("Porfavor, Ingrese su edad: "))
        if edad < 0:
            print("La edad no puede ser negativa. Porfavor, ingrese una edad valida.")
            continue
        break
    except ValueError:
        print("Porfavor, ingrese un número valido para la edad")
        
if edad < 18:
    print("Usted es menor de edad")
else:
    print("Usted es mayor de edad")        
