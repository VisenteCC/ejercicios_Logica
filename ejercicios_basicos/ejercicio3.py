#Solicitar al usuario que ingrese una temperatura en grados Celsius y mostrarla en grados Fahrenheint.
#fahrenheit = (°C * 9/5) + 32

while True:
	temp = input("Porfavor Ingrese la temperatura en C°s: ")
	try:
		celsius = float(temp)
		break
	except ValueError:
		print("Porfavor, ingrese un número valido")
		
fahrenheit = (celsius * 9/5) + 32
print(f"La temperatura en F° es: {fahrenheit}°F")