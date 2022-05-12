from dataclasses import dataclass
from boss import *
from country import *

@dataclass
class Filiale:
    mere: str
    filiale: str
    pdg: Boss
    countryMere: Country
    countryFil: Country

    def isFiliale(self, pdg):
        if (self.mere == Boss.getEntreprise(self.pdg)):
            isfil = True
        else:
            isfil = False
        return isfil

    def maison_mere(self):
        return "la maison mere de " + self.filiale + " est " + self.mere

    def detectFiscalOptimisation(self) -> bool:
        if self.countryMere != self.countryFil:
            print("potentielle optimisation fiscal: taux mere %(first)d et taux fille %(second)d"%{"first": self.countryMere.tauxImposition, "second": self.countryFil.tauxImposition})
            return True
        else:
            print("Pas d evasion fiscale")
            return False
