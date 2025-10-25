from random import randint
from celle import Celle

class Rutenett:
    def __init__(self, rader, kolonner):
        self._ant_rader = rader
        self._ant_kolonner = kolonner
        self._rutenett = []
        self._lag_tomt_rutenett()
        pass

    def _lag_tomt_rutenett(self):
        self._rutenett = [self._lag_tom_rad() for n in range(self._ant_rader)]
        pass

    def _lag_tom_rad(self):
        return [None for n in range(self._ant_kolonner)]
        pass

    def fyll_med_tilfeldige_celler(self):
        for rad in range(self._ant_rader):
            for kol in range(self._ant_kolonner):
                self.lag_celle(rad, kol)
        pass

    def lag_celle(self, rad, kol):
        from celle import Celle
        celle = Celle()
        if randint(0,2) == 0:
            celle.sett_levende()
        self._rutenett[rad][kol] = celle
        pass

    def hent_celle(self, rad, kol):
        if 0 <= rad < self._ant_rader and 0 <= kol < self._ant_kolonner:
            return self._rutenett[rad][kol]
        else:
            return None
        pass

    def tegn_rutenett(self):
        for rad in range(self._ant_rader):
            linje = ""
            for kol in range(self._ant_kolonner):
                celle = self._rutenett[rad][kol]
                linje += celle.hent_status_tegn()
            print(linje)
        pass

    def _sett_naboer(self, rad, kol):
        celle = self.hent_celle(rad, kol)
        if celle is None:
            return #Fuck
        
        for x in (-1, 0, 1):
            for y in (-1, 0, 1):
                if x == 0 and y == 0:
                    continue
                nabo_rad = rad + x
                nabo_kol = kol + y
                nabo_celle = self.hent_celle(nabo_rad, nabo_kol)
                if nabo_celle is not None:
                    celle.legg_til_nabo(nabo_celle)
        pass

    def koble_celler(self):
        for rad in range(self._ant_rader):
            for kol in range(self._ant_kolonner):
                self._sett_naboer(rad, kol)
        pass

    def hent_alle_celler(self):
        return [celle for rad in self._rutenett for celle in rad]
        pass

    def antall_levende(self):
        ant = 0
        for celle in self.hent_alle_celler():
            if celle.er_levende():
                ant += 1
        return ant
        pass

