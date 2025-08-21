#Escribir un programa que calcule la suma de los números del 1 al 100 utilizando un bucle while.
#i = 1
#while i <= 5:
#    print(i)
#    i += 1
#acumulador = 0
#for numero in range(5):
    #acumulador = acumulador + (numero + 1)
    #acumulador += numero + 1

i = 1
acumulador = 0

while i >= 1 and i <= 100:
    acumulador += i 
    print(i)
    i += 1
print("la suma de los numeros es: {}".format(acumulador))