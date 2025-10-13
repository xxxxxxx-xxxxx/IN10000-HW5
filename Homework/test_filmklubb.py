from film import Film
from filmklubb import Filmklubb

def testprogram():

    # __init__
    # Opprett Filmklubb-objekt
    print("oppretter Filmklubb-objekt")
    fk =Filmklubb()

    # les_filmer_fra_fil
    # Les inn filmer fra filen filmer.txt
    print("Leser filmer fra fil")
    fk.les_filmer_fra_fil("filmer.txt")
    print()

    # skriv_ut_alle_filmer
    print("Skriver ut all info om alle filmer:")
    fk.skriv_ut_alle_filmer()
    print()

    # registrer_film
    print("Registrerer ny film")
    fk.registrer_film()
    print("\nEtter registrering:")
    fk.skriv_ut_alle_filmer()
    print()
    
    # Hvis _eq_ er implementert i Film og testes i registrer_film:
    print("Prøver å registrere film som allerede finnes")
    print()    


    # finn_film_tittel
    print("Leter etter film med (start på) usannsynlig tittel")
    assert fk.finn_film_tittel("ZZZ") is None
    print("OK: ingen funn som forventet\n")

    print("Leter etter film med (start på) tittel 'Hidden '")
    funn = fk.finn_film_tittel("Hidden ")
    print("Fant:", funn.hent_tittel() if funn else None)
    print()

    # legg_til_skuespillere
    print("Legg til skuespillere for en film")
    if funn:
        fk.legg_til_skuespillere(funn)
    print("\nAlle filmer etter skuespiller-innlegging:")
    fk.skriv_ut_alle_filmer()
    print()

    # finn_film_periode
    print("Leter etter filmer produsert etter 2000 og før 2024:")
    resultater = fk.finn_filmer_periode(2000, 2024)
    for f in resultater:
        print("-", f.hent_tittel())
    print()

    print("Leter etter filmer produsert etter 2020 og før 2020:")
    tom = fk.finn_filmer_periode(2020, 2020)
    assert tom == []
    print("OK: tom liste som forventet")

testprogram()

if __name__ == "__main__":
    fk = Filmklubb()
    fk.les_filmer_fra_fil("filmer.txt")

    film = fk.finn_film_tittel("Hidden ")
    if film:
        film.ny_skuespiller("Taraji P. Henson", "Katherine Johnson")
        film.ny_skuespiller("Octavia Spencer", "Dorothy Vaughan")

    print("Skriver ut all info om alle filmer:")
    fk.skriv_ut_alle_filmer()