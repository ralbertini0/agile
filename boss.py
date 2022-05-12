from dataclasses import dataclass

@dataclass
class Boss:
    nom: str
    entreprise: str


    def changeEntreprise(self, entr) -> str:
        return entr

    def getEntreprise(self):
        return self.entreprise
