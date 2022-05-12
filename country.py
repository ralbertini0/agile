from dataclasses import dataclass
from capitale import *

@dataclass
class Country:
    nom: str
    tauxImposition: int
    capital: Capitale


    def getTauxImposition(self) -> int:
        return self.tauxImposition

    def tauxCapital(self):
        print("Le taux a " + self.capital + " est " + self.tauxImposition)


