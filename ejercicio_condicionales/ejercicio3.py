#Programa que determina si un número es positivo, negativo o cero.
while True:
    try:
        num = int(input("Porfavor, ingrese un número: "))
        break
    except ValueError:
        print("Ingrese un número válido.")

if num < 0:
    print("Su numero es negativo")
elif num == 0:
    print("Su numero es 0")
else:
    print("Su numero es positivo")    
