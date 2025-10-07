# 5.1 - unksjon for å lage brukernavn
def lag_brukernavn(navn, eksisterende=None):
	navn = navn.lower()
	fornavn, etternavn = navn.split()
	brukernavn = fornavn + etternavn[0]
	
    # Bonus: lag unikt brukernavn
	if eksisterende:
		i = 1
		while brukernavn in eksisterende and i < len(etternavn):
			brukernavn = fornavn + etternavn[:i+1]
			i += 1
	return brukernavn

# 5.2 - Funksjon for å lage e-post
def lag_epost(brukernavn, suffix):
	return f"{brukernavn}@{suffix}"

# 5.3 - Prosedyre for å skrive ut e-poster
def skriv_ut_eposter(brukere):
	print("Alle e-postadresser:")
	for brukernavn, suffix in brukere.items():
		print(lag_epost(brukernavn, suffix))

# 5.3.1 Tester brukerne
assert lag_brukernavn("Kari Nordmann") == "karin"
assert lag_brukernavn("Ola Nordmann") == "olan"
assert lag_epost("karin", "student.matnat.uio.no") == "karin@student.matnat.uio.no"

# 5.4 - Interaktivt program for å legge til brukere med mer
brukere = {}
while True:
	print("Meny:")
	print("1. Legg til ny bruker")
	print("2. Skriv ut alle e-postadresser")
	print("3. Avslutt")
	valg = input("Velg: ")
	if valg == "1":
		navn = input("Skriv inn fullt navn: ")
		suffix = input("Skriv inn e-post suffix: ")
		brukernavn = lag_brukernavn(navn, brukere)
		if brukernavn in brukere:
			print(f"Brukernavn '{brukernavn}' finnes allerede!")
		else:
			brukere[brukernavn] = suffix
			print(f"Bruker lagt til: {brukernavn}")
	elif valg == "2":
		skriv_ut_eposter(brukere)
	elif valg == "3":
		print("Avslutter programmet.")
		break
	else:
		print("Ugyldig valg!")
