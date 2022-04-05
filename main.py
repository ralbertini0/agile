from dataclasses import dataclass
from Boss import Boss
from Filiale import Filiale
import unittest

#import biblio

#install behave

boss1 = Boss("Bernard Arnault", "LVMH")
filiale1 = Filiale("LVMH", "Louis Vuitton")

class FilialeTest(unittest.TestCase):

    def setUp(self):
        self.filiale2 = Filiale("LVMH", "Louis Vuitton")
        self.boss1 = Boss("Bernard Arnault", "LVMH")

    def testIsFiliale(self):
        self.assertEqual(self.filiale2.isFiliale(boss1), True)

if __name__ == '__main__':
    unittest.main()

