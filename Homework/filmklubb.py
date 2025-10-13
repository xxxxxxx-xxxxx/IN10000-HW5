from film import Film

class Filmklubb:
    def __init__(self):
        self._filmer = []

    def les_filmer_fra_fil(self, filnavn: str) -> None:
        try:
            with open(filnavn, "r", encoding="utf-8") as f:
                for linje in f:
                    linje = linje.strip()
                    if not linje:
                        continue
                    if ";" not in linje:
                        continue
                    tittel, år_str = linje.split(";", 1)
                    tittel = tittel.strip()
                    år_str = år_str.strip()
                    try:
                        år = int(år_str)
                    except ValueError:
                        continue
                    self._filmer.append(Film(tittel, år))
        except FileNotFoundError:
            print(f"Filen {filnavn} ble ikke funnet.")

    def skriv_ut_alle_filmer(self) -> None:
        for film in self._filmer:
            film.skriv_ut_film()
            print()

    def registrer_film(self) -> None:
        tittel = input("Tittel: ").strip()
        år_str = input("År (4 siffer): ").strip()
        try:
            år = int(år_str)
        except ValueError:
            print("Feil: År må være et heltall på 4 siffer.")
            return

        ny = Film(tittel, år)
        for f in self._filmer:
            if f == ny:
                print("Feil: Filmen finnes allerede (samme tittel og år).")
                return

        self._filmer.append(ny)
        print("OK: Film registrert.")

    def finn_film_tittel(self, tittel: str):
        for f in self._filmer:
            if f.sjekk_tittel(tittel):
                return f
        return None

    def legg_til_skuespillere(self, film: Film) -> None:
        if film is None:
            print("Ingen film valgt.")
            return
        print("Legg til skuespillere (tomt navn for å stoppe):")
        while True:
            navn = input("  Navn: ").strip()
            if navn == "":
                break
            rolle = input("  Rolle: ").strip()
            film.ny_skuespiller(navn, rolle)
        print("Ferdig med å legge til skuespillere.")

    def finn_filmer_periode(self, år_1: int, år_2: int):
        return [f for f in self._filmer if f.sjekk_periode(år_1, år_2)]