while True:
    num1 = input("Ingrese el primer número: ")
    num2 = input("Ingrese el segundo número: ")
    try:
        num1 = int(num1)
        num2 = int(num2)
        break
    except ValueError:
        print("Por favor, ingrese números válidos.") 

suma = int(num1) + int(num2)
print(f"La suma de {num1} y {num2} es: {suma}")