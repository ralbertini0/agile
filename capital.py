from dataclasses import dataclass

@dataclass
class Capital:
    nom: str
    country: str


    def getCountry(self) -> str:
        return self.country

    def printCapital(self):
        print("la capital de " + self.country + " est " + self.nom)
