from dataclasses import dataclass
from Boss import *

@dataclass
class Filiale:
    mere: str
    filiale: str
    pdg: Boss

    def isFiliale(self, pdg):
        if (self.mere == Boss.getEntreprise(self.pdg)):
            isfil = True
        else:
            isfil = False
        return isfil

    def maison_mere(self):
        return "la maison mere de " + self.filiale + " est " + self.mere

