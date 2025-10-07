# 4.1 Regnefunksjoner
def add(x, y):
	return x + y

def subtract(x, y):
	return x - y

def divide(x, y):
	assert y != 0, "Kanke dele på null din tulling!"
	return x / y

# Tester regnefunksjonene
assert add(2, 3) == 5
assert subtract(5, 2) == 3
assert divide(10, 2) == 5
assert add(-2, 3) == 1
assert subtract(-5, -2) == -3
assert divide(-10, -2) == 5

# 4.2 - Tommer til centimeter
def inches_to_cm(inches):
	assert inches > 0, "Value must be positive!"
	return inches * 2.54

# Tester konvertering
assert inches_to_cm(1) == 2.54
assert inches_to_cm(10) == 25.4

# 4.3 - Input og regnefunksjoner
def write_calculations():
	print("Utregninger:")
	x = float(input("Skriv inn tall 1: "))
	y = float(input("Skriv inn tall 2: "))
	print(f"Resultat av summering: {add(x, y)}")
	print(f"Resultat av subtraksjon: {subtract(x, y)}")
	print(f"Resultat av divisjon: {divide(x, y)}")
	inches = float(input("Konvertering fra tommer til cm: Skriv inn et tall: "))
	print(f"Resultat: {inches_to_cm(inches)}")


# 4.4 -  Meny funksjon av alle mulighetene
def verktoykasse():
	print("Verktoykasse:")
	print("1. Summering")
	print("2. Subtraksjon")
	print("3. Divisjon")
	print("4. Tommer til centimeter")
	choice = input("Velg beregning (1-4): ")
	if choice == "1" or choice == "2" or choice == "3":
		# Sjekk at input er tall
		x_str = input("Skriv inn tall 1: ")
		y_str = input("Skriv inn tall 2: ")
		if not x_str.replace('.', '', 1).isdigit() or not y_str.replace('.', '', 1).isdigit():
			print("Du må skrive inn tall!")
			return
		x = float(x_str)
		y = float(y_str)
		if choice == "1":
			print(f"Resultat av summering: {add(x, y)}")
		elif choice == "2":
			print(f"Resultat av subtraksjon: {subtract(x, y)}")
		elif choice == "3":
			# Sjekk for deling på null
			if y == 0:
				print("Du kan ikke dele på null!")
			else:
				print(f"Resultat av divisjon: {divide(x, y)}")
	elif choice == "4":
		inches_str = input("Skriv inn tommer: ")
		if not inches_str.replace('.', '', 1).isdigit():
			print("Du må skrive inn tall!")
			return
		inches = float(inches_str)
		if inches <= 0:
			print("Du må skrive inn et positivt tall!")
		else:
			print(f"Resultat: {inches_to_cm(inches)}")
	else:
		print("Ugyldig valg!")

# Start programmet
verktoykasse()
