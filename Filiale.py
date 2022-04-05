from dataclasses import dataclass

@dataclass
class Filiale:
    mere: str
    filiale: str

    def __init__(self, mere: str, filiale: str):
        self.mere = mere
        self.filiale = filiale


    def isFiliale(self, boss1):
        isfil = self.isfiliale(boss1)
        return isfil

    def isfiliale(self, boss1):
        if (self.mere == boss1.entreprise):
            isfil = True
        else:
            isfil = False
        return isfil

    def maisonmere(self):
        return "ma maison mere est " + self.mere

