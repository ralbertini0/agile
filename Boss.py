from dataclasses import dataclass

@dataclass
class Boss:
    nom: str
    entreprise: str

    def __init__(self, nom: str, entreprise: str):
        self.nom = nom
        self.entreprise = entreprise

    def changeEntreprise(self, entr) -> str:
        return entr