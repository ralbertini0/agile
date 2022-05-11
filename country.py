from dataclasses import dataclass
from capital import *

@dataclass
class Country:
    nom: str
    tauxImposition: int
    capital: Capital


    def getTauxImposition(self) -> int:
        return self.tauxImposition

    def tauxCapital(self):
        print("Le taux a " + self.capital + " est " + self.tauxImposition)


