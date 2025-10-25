class Celle:
    # Konstruktør
    def __init__(self):
        self._status = "doed"
        self._naboer = []
        self._ant_levende_naboer = 0
        pass
    
    def sett_doed(self):
        self._status = "doed"
        pass

    def sett_levende(self):
        self._status = "levende"
        pass

    def er_levende(self):
        return self._status == "levende"
        pass

    def hent_status_tegn(self):
        if self._status == "levende":
            return "O"
        else:
            return "."
        pass

    def legg_til_nabo(self, nabo):
        self._naboer.append(nabo)
        pass

    def tell_levende_naboer(self):
        self._ant_levende_naboer = 0
        for nabo in self._naboer:
            if nabo.er_levende():
                self._ant_levende_naboer += 1
        pass

    def oppdater_status(self):
        if self.er_levende():
            if self._ant_levende_naboer < 2 or self._ant_levende_naboer > 3:
                self.sett_doed()
            else:
                self.sett_levende()
        else:
            if self._ant_levende_naboer == 3:
                self.sett_levende()
            else:
                self.sett_doed()
        pass