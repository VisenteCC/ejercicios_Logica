#Programa que determina si un número ingresado está en el rango de 1 a 10.
while True:
    try:
        num = int(input("Porfavor, Ingrese un número: "))
        break
    except ValueError:
        print("Porfavor ingrese un número válido")

if num >= 1 and num <= 10:
    print("El numero ingresado si esta entre el rango de 1 al 10.")

else:
    print("Su numero ingresado no estra entre el rango de 1 al 10.")