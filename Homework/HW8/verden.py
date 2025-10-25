from rutenett import Rutenett

class Verden:
    def __init__(self, rader, kolonner):
        self._rutenett = Rutenett(rader, kolonner)
        self._generasjonsnummer = 0
        self._rutenett.fyll_med_tilfeldige_celler()
        self._rutenett.koble_celler()
        pass

    def tegn(self):
        self._rutenett.tegn_rutenett()
        print(f"Gen: {self._generasjonsnummer}")
        print(f"Levende: {self._rutenett.antall_levende()}")
        pass

    def oppdatering(self):
        alle = self._rutenett.hent_alle_celler()
        for celle in alle:
            celle.tell_levende_naboer()
        for celle in alle:
            celle.oppdater_status()
        self._generasjonsnummer += 1
        pass
