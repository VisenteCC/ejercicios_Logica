#Solicitar al usuario ingresar dos números. 
#Si el primero es mayor que el segundo se deben sumar ambos números, en caso contrario se deben restar.
while True:
    try:
        num = int(input("Porfavor, ingrese un número: "))
        break
    except ValueError:
        print("ingrese un número válido")

while True:
    try:
        num_2 = int(input("Porfavor, ingrese el segundo número: "))
        break
    except ValueError:
        print("ingrese un número válido")        
if num > num_2:
    suma = num + num_2
    print(f"Como el primer numero ingresado es mayor que el segundo entonces se sumo: {suma}") 
else:
    resta = num - num_2
    print(f"Como el primer numero ingresado es menor que el segundo entonces se resto: {resta}")    
