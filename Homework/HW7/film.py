class Film:
    def __init__(self, tittel:str, år:int):
        self._tittel: str = tittel
        self._år: int = år
        self._skuespillere: dict[str, str] = {}

    def hent_tittel(self):
        return self._tittel
    
    def ny_skuespiller(self, navn:str, rolle:str):
        if navn not in self._skuespillere:
            self._skuespillere[navn] = rolle
        else:
            print(f"Skuespilleren {navn} er allerede registrert med rollen {self._skuespillere[navn]}")
    
    def hent_skuespiller_navn(self):
        return sorted(list(self._skuespillere.keys()))
    
    def skriv_ut_film(self):
        print(f'{self._tittel} utgitt i ({self._år})')
        if self._skuespillere:
            print("Skuespillere:")
            for navn, rolle in self._skuespillere.items():
                print(f" - {navn} som {rolle}")
        else:
            print("Ingen skuespillere registrert.")

    def sjekk_periode(self, år_1: int, år_2: int) -> bool:
        return år_1 < self._år < år_2
    
    def sjekk_tittel(self, tittel_start: str) -> bool:
        if tittel_start == "":
            return True
        if len(tittel_start) > len(self._tittel):
            return False
        return self._tittel.startswith(tittel_start)
    
    def __str__(self) -> str:
        linjer = [f"Tittel: {self._tittel}", f"År: {self._år}"]
        if not self._skuespillere:
            linjer.append("Skuespillere: (ingen registrert)")
        else:
            linjer.append("Skuespillere:")
            for navn, rolle in sorted(self._skuespillere.items()):
                linjer.append(f" - {navn}: {rolle}")
        return "\n".join(linjer)

    def __eq__(self, annen: object) -> bool:
        if not isinstance(annen, Film):
            return NotImplemented
        return (self._tittel == annen._tittel) and (self._år == annen._år)
