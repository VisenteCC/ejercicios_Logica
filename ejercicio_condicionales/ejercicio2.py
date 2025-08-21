#Programa que determina si un número es par o impar.
while True:
    try:
        num = int(input("Porfavor, Ingrese un número: "))
        break
    except ValueError:
        print("Porfavor, ingrese un número valido")
if num % 2 == 0:
    print(f"El número {num} es par.")
else:
    print(f"El número {num} es impar.")