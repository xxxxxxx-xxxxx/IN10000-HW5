from film import Film


def test_film():
    print("Oppretter to filmer")
    a1 = Film("Hidden Figures", 2016)
    a2 = Film("The Imitation Game", 2014)

    # hent_tittel
    # Skriv ut tittel på de to filmene
    print("Skriver ut titler på to filmer")
    print(a1.hent_tittel())
    print(a2.hent_tittel())
    print()

    # ny_skuespiller
    # Legg til to skuespillere og deres roller for en av filmene, skriv ut alt om filmen
    print("Legger til to skuespillere")
    a1.ny_skuespiller("Taraji P. Henson", "Katherine Johnson")
    a1.ny_skuespiller("Octavia Spencer", "Dorothy Vaughan")
    a1.ny_skuespiller("Taraji P. Henson", "Katherine Johnson")
    print()

    # Prøv å legge inn en av skuespillerne igjen, med en ny rolle, og sjekk at rollen ikke blir endret
    print("Tester ulovlig innlegging av skuespiller")
    a1.ny_skuespiller("Taraji P. Henson", "Katherine Johnson")

    # hent_skuespiller_navn
    print("Henter og skriver ut alle skuespillernavn for en film:")
    for navn in a1.hent_skuespiller_navn():
        print("-", navn)
    print()

    # skriv_ut_film
    # Skriv ut all informasjon om begge filmer du har lagt inn
    print("Skriver ut all info om to filmer:")
    a1.skriv_ut_film()
    print()
    a2.skriv_ut_film()
    print()

    # hent_alle_skuespiller_navn
    # Skriv ut skuespillernes navn for den filmen som har to
    # print("Henter og skriver ut alle skuespillernavn for en film:")
    # <fyll ut og fjern # på print-setningen>

    # sjekk_periode
    # Sjekk om en film du har lagt inn er i en periode du velger
    # (velg periode som skal gi True og sjekk at dette blir resultatet)
    print("Sjekker at en film er i oppgitt periode")
    print(a1.sjekk_periode(2010, 2020))  # forventer True for 2016

    print("Sjekker at en film ikke kan være produsert før og etter samme år")
    print(a1.sjekk_periode(2016, 2016))  # forventer False (strengt mellom)

    # <fyll ut og fjern # på print-setningen>

    # Sjekk om en film er i en periode som skal gi False
    # (velg samme årstall til begge argumenter og sjekk resultat er False)
    # print ("Sjekker at en film ikke kan være produsert før og etter samme år")
    # <fyll ut og fjern # på print-setningen>

    # sjekk_tittel
    print("Sjekker om starten på en films tittel kjennes igjen")
    print(a1.sjekk_tittel("Hidden"))      # forventer True (starten matcher)
    print(a1.sjekk_tittel(""))            # forventer True (tom streng)
    print(a1.sjekk_tittel("Hidden F"))    # forventer True (prefiks)
    print(a1.sjekk_tittel("hidden"))      # forventer False (case-sensitive)
    print(a1.sjekk_tittel("Hidden Figures!"))  # lengre enn tittel -> False

    # __str__
    print("Skriver ut en film med print (test av __str__)")
    print(a1)   # dette kaller __str__ automatisk
    print()
    print()

    # test __eq__ (frivillig)
    print("Tester __eq__ med to ulike filmer:")
    print(a1 == a2)  # forventer False
    print("Tester __eq__ med to like filmer:")
    b1 = Film("Hidden Figures", 2016)
    print(a1 == b1)  # forventer True

test_film()