# Oppgave 1.1 - En funksjon som legger til to tall

def adder(tall1, tall2):
	return tall1 + tall2


# Liste/array data legges inn
while True:
	tall = []
	tall.append(int(input("Skriv inn tall 1: ")))
	tall.append(int(input("Skriv inn tall 2: ")))
	resultat = adder(tall[0], tall[1])
	print(f"The sum of {tall[0]} + {tall[1]} = {resultat}")
	svar = input("One more time? (yes/no): ").strip().lower()
	if svar != "yes":
		print("Moving on...")
		break

# Oppgave 1.2/1.3 - En funksjon som teller bokstaver i en setning eller ord
print("What about counting the amount of times a letter is in a sentence?")
lc = input("Do you want to count letters? (yes/no): ").lower()
if lc == "yes":

# Loopen som teller om du vil flere ganger eller ikke
	while True:
		text = input("Enter a sentence or word: ")
		letter = input("Enter a letter to count: ")
		count = text.count(letter)
		print(f"The letter '{letter}' occurs {count}x times in the sentence/text.")
		again = input("Count again? (yes/no): ").lower()
		if again != "yes":
			print("Shutting down...")
			break